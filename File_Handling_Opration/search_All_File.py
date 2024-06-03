import re  # Import the 're' module for regular expression operations

txt = "The rain in Spain"  # Define a string variable 'txt' with the value "The rain in Spain"

x = re.findall("ai", txt)  # Use the re.findall() function to find all occurrences of the pattern "ai" in 'txt'
                            # and assign the result to the variable 'x'

print(x)  # Print the value of 'x'