# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
# string_input= "You would never guess what can happen when you jump into a seemingly s"
# letter_input = "g"

string_input= input("Write a few words: ")
letter_input = input("Choose a letter from your phrase:")
if letter_input == '':
    letter_input = input("Choose a letter from your phrase:")

if letter_input in string_input:
    # result = string_input.find(letter_input)
    result = string_input.index(letter_input)
    print(f'The index of first occurrence of the letter "{letter_input}" in your phrase :  {result}')
else:
    print('This letter is missing from your phrase')

