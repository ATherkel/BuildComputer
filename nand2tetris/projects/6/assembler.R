



## ---- initialize ----

library(data.table)
library(magrittr)



#### ---- import script ----


asm <- data.table(code = script)


#### ---- predefined symbols ----
symboltable <-
    data.table(
        symbol = c(
            paste0("R", 0:15),
            "SCREEN",
            "KBD",
            "SP",
            "LCL",
            "ARG",
            "THIS",
            "THAT"
        ),
        value = c(0:15,
                  2 ^ 14,
                  2 ^ 14 + 2 ^ 13,
                  0:4)
    )




## ---- pgm ----

#### ---- Remove whitespace and comment lines. ----
## Remove whitespace and comment lines
asm[, code :=
        gsub(x = code,
             pattern = "\\s*|(^\\s*//.*$)",
             replacement = "")]
## Remove empty lines
#asm <- asm[code != ""]
asm

## ---- first pass ----
# scan the entire program:
# for each "(XXXX)" instruction, 
#   add (XXXX, address) to the symbol table
#   where address is the number of instruction following (XXXX)

#### ---- Add row numbers ----
rx_label <- "^\\((.*)\\)$"
asm[code != "" & 
        !grepl(pattern = rx_label,
             x = code), 
    row := .I - 1]
asm

#### ---- Identify labels ----
## If pattern (XXXX), use the shift function to take the next (lead)
## value of row (the row of the following instruction), 
## otherwise take the row. Excludes comment rows.
asm[code != "",
    value := ifelse(
        grepl(pattern = rx_label,
              x = code),
        zoo::na.locf(row, fromLast = TRUE),
        row)]
asm

#### ---- Add labels to symbol table ----
labels <-
    asm[grep(pattern = rx_label, x = code),
        .(symbol = gsub(
            pattern = rx_label,
            replacement = "\\1",
            x = code
        ), value)]
labels

if(!any(labels[,symbol] %in% symboltable[,symbol])){
    symboltable <- rbind(symboltable, labels)
}
symboltable

## Delete label rows
asm <- asm[!grepl(pattern = rx_label, x = code)]

## ---- second pass ----
# Set n to 16
# scan the entire program again; for each instruction:
#   1) if the instruction is @symbol, look uo symbol in the symbol table
#       if (symbol, value) is found use value
#       if not found:
#           add (symbol, n) to symbol table
#           use n to complete instruction's translation
#           n++
#   2) if c-instruction, complete instruction's translation
#   3) write translation to output

#### ---- Identify variables ----

rx_a <- "^\\@([^0-9].*)"

asm[grep(x = code,pattern = rx_a),
    symbol := gsub(pattern = rx_a,
         replacement = "\\1",
         x = code)]
asm
suppressWarnings(
newvar <- 
    asm[!symboltable, 
              on = .(symbol)] %>% 
    .[!is.na(symbol),
     .(symbol, value)] %>% 
    .[,min(value), by = symbol]
)
newvar[, `:=`(value = .I + 15,
              V1 = NULL)]
newvar


if(!any(newvar[,symbol] %in% symboltable[,symbol])){
    symboltable <- rbind(symboltable, newvar)
}

symboltable


## ---- @ handling vars ----
asm[symboltable, on = .(symbol), instructionDec := i.value]

## ---- @ handling nums ----
asm[grepl(pattern = "^\\@\\d", x = code) & is.na(instructionDec), 
    instructionDec := 
        gsub(pattern = "^@(.*)",
             replacement = "\\1",
             x = code) %>% 
        as.numeric]




# asm[, type :=
#         ifelse(grepl(x = code, pattern = "^\\@",),
#                "A",
#                "C")]

## ---- c instruction ----

#### ---- instruction tables ----
comp_a <- c(0,1,-1,"D","A","!D","!A",
            "-D","-A","D+1","A+1",
            "D-1","A-1",
            "D+A","D-A",
            "A-D","D&A","D|A")
comp_m <- gsub("A", "M", comp_a)

comp <- data.table(
    comp = c(comp_a,comp_m),
    a = c(rep(0, 18), rep(1,18)),
    c1 = c(1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0),
    c2 = c(0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1),
    c3 = c(1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0),
    c4 = c(0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1),
    c5 = c(1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0),
    c6 = c(0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1))
comp

dest <- data.table(
    dest = c("","M","D","MD","A","AM","AD","AMD"),
    d1 = c(0,0,0,0,1,1,1,1),
    d2 = c(0,0,1,1,0,0,1,1),
    d3 = c(0,1,0,1,0,1,0,1))
dest

jump <- data.table(
    jump = c("",
      "JGT","JEQ","JGE",
      "JLT","JNE","JLE","JMP"),
    j1 = c(0,0,0,0,1,1,1,1),
    j2 = c(0,0,1,1,0,0,1,1),
    j3 = c(0,1,0,1,0,1,0,1))



tobintable <- function(dt){
    name <- colnames(dt)[1]
    ## Collapse the data into one column
    dt[, bin := do.call(paste0,c(.SD)), .SDcols = -1]
    ## Identify duplicates accidentally and erroneously created
    dt[, row := .I[1], by = name]
    dt[, rn := .I]
    ## Remove duplicates
    keeprows <- dt[rn == row]
    ## Remove helper columns
    keeprows[, c("row", "rn") := NULL]
    ## Keep only name and binary value
    keeprows[, setdiff(colnames(keeprows), c(name,"bin")) := NULL]
    
    dt[, c(names(dt)) := NULL]       # Clear existing columns
    dt[, names(keeprows) := keeprows]  # Copy filtered data back
}

tobintable(comp)
tobintable(dest)
tobintable(jump)


#### ---- identify ----

rx_instruction <- "(?:([AMD]*)=)?(!?[AMD\\|&\\+-10]+);?(J\\w{2})?"
c_ins <- function(grp, col, rx){
    gsub(pattern = rx,
         replacement = paste0("\\",grp),
         x = col)
}



asm[is.na(instructionDec),
    `:=`(
        dest = c_ins(1,code,rx_instruction),
        comp = c_ins(2, code, rx_instruction),
        jump = c_ins(3, code, rx_instruction))
    ]
asm[is.na(instructionDec)]



asm[dest, on = .(dest), destbin := i.bin]
asm[comp, on = .(comp), compbin := i.bin]
asm[jump, on = .(jump), jumpbin := i.bin]

asm[is.na(instructionDec) & code != "",
    instruction := paste0(111,compbin,destbin,jumpbin)]

toBits <- function (x, nBits = 16){
    paste(tail(rev(as.numeric(intToBits(x))),nBits), collapse = "")
}

asm[!is.na(instructionDec), 
    instruction := sapply(instructionDec, toBits)]
