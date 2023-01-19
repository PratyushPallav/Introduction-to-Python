a,b,c = input("Enter 3 numbers").split(',')
a = int(a)
b = int (b)
c = int (c)
if(a>b and a>c):
    print("{} is the largest amongst {} and {}".format(a,b,c))
elif(b>a and b>c):
    print("{} is the largest amongst {} and {}".format(b,a,c))
elif(c>a and c>b):
    print("{} is the largest amongst {} and {}".format(c,b,a))
else:
    print("Either two or all three numbers are equal")