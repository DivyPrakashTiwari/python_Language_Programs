import re  # Import the 're' module for regular expression operations

txt = "The rain in Spain"  # Define the input string 'txt'

x = re.search("r", txt)  # Search for the first occurrence of the letter 'r' in 'txt'
print(x)  # Print the match object 'x' containing information about the match