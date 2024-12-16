# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

print(""" == Investments == """)

investment_amount = int(input("How much would you like invest ? : "))
interest_rate = int(input("Under what percentage ? % "))
years_invest =int(input("For how many years ?"))

# investment_amount = 100000
# interest_rate = 10
# years_invest = 5

result =int(investment_amount *(1 + interest_rate/100)**years_invest - investment_amount)
print(f"Your income will be  = {result}")