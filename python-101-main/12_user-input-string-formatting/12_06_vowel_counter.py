# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

s_input = input("Enter a few words ")
vowels = "aeiouy"
# s_input = ""
vowel_a = s_input.count('a')
vowel_e = s_input.count('e')
vowel_i = s_input.count('i')
vowel_o = s_input.count('o')
vowel_u = s_input.count('u')
vowel_y = s_input.count('y')

print(f"Your phrase contains :\n"
      f"a = {vowel_a}\n"
      f"e = {vowel_e}\n"
      f"i = {vowel_i}\n"
      f"o = {vowel_o}\n"
      f"u = {vowel_u}\n"
      f"y = {vowel_y} ")





