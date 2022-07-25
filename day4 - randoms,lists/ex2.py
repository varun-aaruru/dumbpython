
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

length = len(names)
winnerchoice = random.randint(0, length-1)
winner = names[winnerchoice]
print(f"{winner} is going to buy the meal today!")

# instead of all above we can use random.choice() method
#winner = random.choice(names)
#print(f"{winner} is going to buy the meal today!")
