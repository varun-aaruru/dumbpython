# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if (size == "S" or size == "s"):
    bill = 15
elif (size == "M" or size == "m"):
    bill = 20
elif (size == "L" or size == "l"):
    bill = 25
if (add_pepperoni == "Y" or add_pepperoni == "y"):
    if (size == "S" or size == "s"):
        bill += 2
    else:
        bill += 3
if (extra_cheese == "Y" or extra_cheese == "y"):
    bill += 1

print(f"Your final bill is: ${bill}")
