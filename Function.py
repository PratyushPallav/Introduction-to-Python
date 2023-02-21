def func(a,b=-5):
    if(a>b):
        print('a = {}'.format(a))
    else:
        print('b = {}'.format(b))
#func(15)
#func(15,25) # it will overwrite the value of b to 25

def func1(a,b,c=2):
    print(a+b+c)
#func1(2,c=4)
#func1(2,4,5)
#func1(2,4)

lst = [1,2,3]
l = list(map(square,list))

