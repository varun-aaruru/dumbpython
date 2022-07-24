# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("************Tip Calculator****************")
billAmount = float(input("Enter your bill amount in dollars\n"))
numberOfPeople = int(input("How many people will split the bill?\n"))
tipPercentage = float(input("How much you want to tip?(in percentage)\n"))
tipAmount = billAmount*tipPercentage/100
finallBill = billAmount+tipAmount
eachPersonAmount = '{0:.2f}'.format(finallBill/numberOfPeople)
message = f"Each person should pay {eachPersonAmount}$"
print(message)
