# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
num = input('Choose a number between 1 and 1 000 000 000: ')
# num = '666'
if int(num) % 3 == 0 :
    print("The entered number is divisible by three")
else:
    print('The entered number is not divisible by three')