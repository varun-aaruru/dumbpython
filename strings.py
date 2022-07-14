exampleString = "welcome to India!"
anotherString = "Have a great trip!"
print(exampleString[:5])
# welco
print(exampleString[::-1])
# !aidnI ot emoclew
print(exampleString[4::-1])
# oclew i.e,reverse from 4th index
print(exampleString[4:13:2])
# oet n i.e,every 2nd element from 4th to 13th index
print(exampleString[12:3:-1])
# nI ot emo i.e, reverse from 12th index to 3rd index
print(exampleString.upper())
print(exampleString.isnumeric())
print(exampleString.find('I'))
print(exampleString.index('I'))
# difference between index and find
######index##########
# 1.Returns an exception if substring isn’t found
# 2.It shouldn’t be used if you are not sure about the presence of the substring
# 3.This can be applied to strings, lists and tuples
# 4.It cannot be used with conditional statement
######find###########
# 1.Returns -1 if substring isn’t found
# 2.It is the correct function to use when you are not sure about the presence of a substring
# 3.This can only be applied to strings
# 4.It can be used with conditional statement to execute a statement if a substring is found as well if it is not
print(exampleString.split(" "))
print(exampleString.replace("welcome", "Welcome"))
print(exampleString.rpartition(" "))
print(exampleString.rpartition(" to "))
print(exampleString+" "+anotherString)
