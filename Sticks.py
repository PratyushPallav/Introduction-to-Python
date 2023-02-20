stick = 21
while True:
    s = int(input("Pick stick (1-4)"))
    if(s>4 or s<1):
        print("Invalid, Pick (1-4) only")
        continue
        computer = 5-s
        stick -= (s+computer)
        if(stick == 1):
            print("Loosen")
            break
        else:
            print(computer)
