# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

# word_1 = "hello"
# word_2= "world"
# word_3 = 'greetings'

word_1 = input('Enter the first word : ')
word_2 = input('Enter the second word : ')
word_3 = input('Enter the third word : ')


list_words= [word_1,word_2,word_3]
len_word = 0
for word in list_words:
    if len_word < len(word):
        longest_word = word
print(f" The longest word is {longest_word} and it contains {len(longest_word)} letters")

