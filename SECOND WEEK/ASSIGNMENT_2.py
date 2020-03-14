# This program will calculate the prime numbers within a range of numbers

number=int(input("enter the number that you will want the prime numbers here "))
# Every number you provide is assumed that you will be counting from 2 onwards to
# to that number.
for p in range(2,number+1):
    if p>1:
        for i in range(2,p):
            if (p%i)==0:
                break
        else:
            print("This is correct",p)



    



    


