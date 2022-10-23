# Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. 
# The comparison should be case-insensitive.

string = "I love software engineering"

sorted_string = sorted (string.split(), key = str.lower)
print(sorted_string)