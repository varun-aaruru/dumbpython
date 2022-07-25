# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight/(height**2))
if bmi > 35:
    condition = "clinically obese"
elif 30 < bmi < 35:
    condition = "obese"
elif 25 < bmi < 30:
    condition = "slightly overweight"
elif 18.5 < bmi < 25:
    condition = "normal weight"
else:
    condition = "underweight"
if condition == "normal weight":
    print(f'"Your BMI is {bmi}, you have a {condition}"')
else:
    print(f'"Your BMI is {bmi}, you are {condition}."')
