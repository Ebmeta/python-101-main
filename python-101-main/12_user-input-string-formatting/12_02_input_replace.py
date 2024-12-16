# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
from os import replace

# string_input = "more python programming please"
# symbol_input = '§'
string_input = input("Write a few words:")
symbol_input = input("Write any symbol:")
result = string_input.replace(string_input[0], symbol_input)


print(result)