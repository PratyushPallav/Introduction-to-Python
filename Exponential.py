x = float(input("Enter the value of x"))
i = 1
s,p = 1.0,1.0
while(p>=0.0001):
    p = p*(x/i)
    s+=p
    i+=1
print("Exponential({}) = {}".format(x,s))