# This program will calculate the number of miles per a galon.

total_mile=float(input("Input the total mile covered in the journey here"))
full_tank=float(input("Input the number of galons used for the full tank here"))
print("Miles per a galon =",float(total_mile/full_tank))

print("Question 3.4")
five_digit_number=input("Input a five digit number here ")
for i in five_digit_number:
    print(i,end="")
print("=",end="")
for p in five_digit_number[::-1]:
    print(p,end="")
    if i==p:
        print("Palazium")
    else:
        print("Not Correct")


