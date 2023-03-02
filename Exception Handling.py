import math
a,b = input("Enter two numbers").split(',')
a = int(a)
b = int(b)
q = a/b
r = a%b
#d = divmod(a,b)
#print(d)
while(True):
    try:
        if(b==0):
            raise DividedByZero
        else:
            print(q)
            break
    except DivideByZero:
        print("Divided by Zero")
        print("Input next")
    try:
        if(type(a)==int and type(b)==int):
            raise NotIntegerType
        else:
            print(q)
            print(r)
            break
    except NotIntegerType:
        print("Not of integer type")
        print("Input next")
