# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
totalname = (name1+name2).lower()
t_count = totalname.count('t')
r_count = totalname.count('r')
u_count = totalname.count('u')
e_count = totalname.count('e')
l_count = totalname.count('l')
v_count = totalname.count('o')
o_count = totalname.count('v')
e_count = totalname.count('e')
truecount = t_count+r_count+u_count+e_count
lovecount = l_count+o_count+v_count+e_count
truelovecount = int(str(truecount)+str(lovecount))
if truelovecount < 10 or truelovecount > 90:
    print(
        f"Your score is {truelovecount}, you go together like coke and mentos.")
elif truelovecount > 40 and truelovecount < 50:
    print(f"Your score is {truelovecount}, you are alright together.")
else:
    print(f"Your score is {truelovecount}")
