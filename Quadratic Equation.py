import math
def exporoot(a,b,c):
    dis = (b*b)-(4*a*c)
    sq_root = math.sqrt(abs(dis))
    if(dis > 0):
        print("Real and different roots")
        root1 = (-b+sq_root)/(2*a)
        root2 = (-b-sq_root)/(2*a)
        print("First root = {}".format(root1))
        print("Second Root = {}".format(root2))
    elif(dis == 0):
        print("Real and Same root")
        root1 = -b/(2*a)
        print("Root of the equation is {}.".format(root1))
    else:
        print("Complex roots")
        root1 = - b / (2 * a), "+ i", sq_root
        root2 = - b / (2 * a), " - i", sq_root
        print("First root = {}".format(root1))
        print("Second Root = {}".format(root2))
a,b,c = input("Enter the values of a,b and c").split(',')
a = int(a)
b = int(b)
c = int(c)
if(a==0):
    print("Not a Quadratic Equation")
else:
    exporoot(a,b,c)