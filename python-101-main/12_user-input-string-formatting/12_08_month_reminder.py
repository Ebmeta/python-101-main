# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

num= int(input(" Enter a number between 1 and 12 : "))

months = ["January", "February", 'March' , "April", 'May', 'June', 'July', 'August',
           'September', 'October', 'November' , 'December']
if 0 < num < 13:
    print(f" You choose {months[num-1]} month")
else :
    print('Error ')
