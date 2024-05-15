

# https://chat.openai.com/share/40c7964c-0f2f-44d2-81c7-e88d6a1868a1
def changeExtension(string : str, newExtension : str):
    """
    """
    if not isinstance(string, str):
        raise TypeError("Input <string> must be a string")
    if not isinstance(newExtension, str):
        raise TypeError("Input <newExtension> must be a string")
    
    # Regex pattern to capture the base name and extension
    # https://regex101.com/r/SkENd5/1
    regex = r"^(?P<base>[^.].*\.)(?P<extension>\w+)$|(?P<fullname>^.*$)"

    # Replace the extension with the new extension
    new_string = re.sub(
        regex, 
        lambda m: (
            m.group('base') + newExtension 
            if m.group('base') 
            else m.group('fullname')
        ), 
        string)
    
    return new_string


def writelines(input_data : str | list, filename) -> None:
    """
    Write the given string or list of strings to the specified file.

    Args:
        input_data (str | list): The string or list of strings to write to the file.
        filename (str): The name of the file to write to.

    Raises:
        TypeError: If input_data is neither a string nor a list, or if filename is not a string.
        ValueError: If filename is an empty string.
        IOError: If there is an issue writing to the file.

    Returns:
        None
    """
    # Check input types
    if not isinstance(input_data, (str, list)):
        raise TypeError("Input data must be a string or a list of strings")
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")
    
    # Check filename is not empty
    if not filename:
        raise ValueError("Filename cannot be an empty string")

    # Open the file in write mode
    try:
        with open(filename, 'w') as file:
            # Write data to the file
            if isinstance(input_data, str):
                file.write(input_data)
            else:
                file.writelines(input_data)
    except IOError as e:
        raise IOError("Error writing to file: " + str(e))








