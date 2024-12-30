# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
word = "blood"
# Print an explanation to the user
print('You have to guess a five-letter word. You will have five attempts')
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
hidden_word = "_____"
# Create a counter for how many tries a user has
attempt = 0
while attempt < 5:
# Ask for user input
    enter_letter = (input("Enter one letter : ")).lower()
# Allow only single-character alphabetic input
    if enter_letter.isalpha() == False or len(enter_letter) > 1 :
        enter_letter = input("Try entering the letter again: ")

    for i in range (len(word)):
        if enter_letter == word[i]:
            hidden_word = hidden_word[:i] + enter_letter + hidden_word[i + 1:]


    attempt += 1
    print(f"you have {5-attempt} attempts and open: {hidden_word} ")
    if hidden_word == word:
        print("You won!!")
        break
if hidden_word != word:
    print("Sorry , try again.")






# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it
