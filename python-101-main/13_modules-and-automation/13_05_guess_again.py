# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
num = random.randint(1,10)
# num = 5
sum = 1

while sum < 4:
    guess = input(f"guess a number between 1 and 10 . You have {4-sum} attempts: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    elif sum == 3:
        print(" You loose")
        break
    else:
        print("Try again !")
    sum += 1