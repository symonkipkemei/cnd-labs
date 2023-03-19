# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.



print("Hello user we are going to calculate your profits of your investment\nKindly provide the following details")
principal = int(input("Insert investment amount: "))
interest_rate = int(input("Interest rate in percentage: "))
interest_rate = interest_rate/100
no_years = int(input("Number of year invested: "))

future_value = principal * (1 + (interest_rate/1))**no_years

print(f'The future value is {future_value}')