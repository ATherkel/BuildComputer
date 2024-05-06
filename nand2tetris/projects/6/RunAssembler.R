rstudioapi::getActiveDocumentContext()$path %>%
    dirname %>%
    setwd


out <- "Add"
out <- "Max"
out <- "Rect"
out <- "Pong"


script <- 
    readLines(con = paste0(tolower(out),
                           "/",
                           out,
                           ".asm"))

assembler <- function(script, outfile){
    source("assembler.R")
    
    ## All instructions must be exactly 16 bit 
    ## binary numbers
    if(asm[!grepl("^[01]{16}$",
                  instruction) &
           code != ""] %>% nrow %>% equals(0) %>% not){
        asm[!grepl("^[01]{16}$",
                   instruction) &
                code != ""] %>% print
        stop("asm[code != '', instruction] contains non 16 binary numbers")
    }
    
    writeLines(asm[code != "",
                   instruction],
               con = outfile)
}


assembler(script, paste0(out, ".hack"))


