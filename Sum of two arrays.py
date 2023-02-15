import array as ar
a = ar.array('i',[1,2,3,8])
b = ar.array('i',[4,5,6,9])
for i in range(0,4):
    print(a[i]+b[i])