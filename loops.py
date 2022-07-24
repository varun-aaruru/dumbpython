a = int(input("enter a multiple of 7\n"))
while a % 7 != 0:
    a = int(input("enter a multiple of 7\n"))
else:
    print("%d is multiple of 7" % a)
