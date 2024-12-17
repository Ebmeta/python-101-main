# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

# opinion = input("Enter your honest opinion: ")
opinion = "hello world... dfer"
n=1
last_upper = 0
result=''
for letter in opinion:
    if opinion[0].islower():
        if letter.isalpha():
            if n % 2 == 0:
                letter = letter.upper()
                last_upper = letter
            result += letter
            n += 1
        else:
            result += letter



print("Smile : " ,result)
