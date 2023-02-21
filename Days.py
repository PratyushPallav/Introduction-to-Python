day,month,year = input("Enter today's date (dd,mm,yy)").split(',')
day = int(day)
month = int(month)
year = int(year)
tom,yes=0,0
if(day<=31 and month<=12):
    if(month==5 or month==7 or month==8 or month==10 and day==31):
      tom = 1
      monthp = month
      monthn = month+1
      yes = day-1
      print("Next Day = {},{},{}".format(tom,monthn,year))
      print("Yesterday = {},{},{}".format(yes,monthp,year))
    elif(month==12 and day==31):
        tom = 1
        month = 1
        year = year+1
        yes = day-1
    elif(month==4 or month==6 or month==9 or month==11 and day==30):
        tom = 1
        monthn = month+1
        monthp = month
        yes = day-1
        print("Next Day = {},{},{}".format(tom, monthn, year))
        print("Yesterday = {},{},{}".format(yes, monthp, year))
    elif(month==2 and day==28):
        tom = 1
        month = month+1
        yes = day-1
    elif(month==2 and day==29):
        tom = 1
        month = month+1
        yes = day-1
    elif (month==5 or month==7 or month==8 or month==10 and day==1):
        tom = day+1
        yes = 30
        monthp = month-1
        monthn = month
        print("Next Day = {},{},{}".format(tom, monthn, year))
        print("Yesterday = {},{},{}".format(yes, monthp, year))

    elif(month==4 or month==6 or month==9 or month==11 and day==1):
        tom = day+1
        month = month-1
    elif(month==1 and day==1):
        tom = day+1
        month = 12
        year = year-1
        yes = 31
    elif(month==3 and day==1):
        if(year%2==0):
            yes = 29
        else:
            yes = 28
    else:
        yes=day-1
        tom=day+1