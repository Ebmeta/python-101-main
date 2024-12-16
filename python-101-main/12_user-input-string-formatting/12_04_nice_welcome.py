# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
name = input("Enter your name ")
# name= "Valera Popov"

if " " in name and name[0] != ' ':
    index = name.find(" ")
    name = name[:index]
else:
    name = input("Enter your name ")


print(f" Warm greetings, {name} !")