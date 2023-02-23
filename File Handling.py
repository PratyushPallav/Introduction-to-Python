#fobj = open("text.txt","w")
#fobj.write("Debanshu is a ******* \n")
#fobj.write("Whereas Pratyush is !!!!!!!!")
#print("using print",file=fobj)
#fobj.close()

#Reading Mode
#with open("text.txt") as fobj:
    #for r in fobj:
        #print(r)

#Appending mode
fobj = open("text.txt","a")
fobj.write("Append")
fobj.close()
