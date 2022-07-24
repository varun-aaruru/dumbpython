# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
age = int(input("enter your age: "))
remainingAge = 90-age
message = f"You have {remainingAge*365} days, {remainingAge*52} weeks, and {remainingAge*12} months left."
print(message)
