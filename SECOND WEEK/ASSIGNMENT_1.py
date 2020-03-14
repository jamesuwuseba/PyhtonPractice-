# This program will tell you the class of the your entered number belongs.

number=input('Input any number here ')
seq=len(number)
if seq==1:
    print(number,"is in unit")
elif seq==2:
    print(number,"is in tens")
elif seq==3:
    print(number,'is in hundred')
elif seq==4 or seq==5 or seq==6:
    print(number,'is in thousand')
elif seq==7 or seq==8 or seq==9:
    print(number,'is in millions')
elif seq==10 or seq==11 or seq==12:
    print(number,'is in billions')
elif seq==13 or seq==14 or seq==15:
    print(number,'is in trillions')
else:
    print(number,"does not exist")

    
        
