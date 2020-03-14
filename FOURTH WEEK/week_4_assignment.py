# This program will read 20 numbers in a list and only print the number when there is no duplication.

# numbers=[1,1,1,3,4,5,5,6,7,8,9,10,4,13,14,86,64,43,21,53]

# number=[]
# for p in range(20):
#     a=(input("Enter your number here"))
#     print(number)
#     if a not in number:
#         print(a)
#     number.append(a)

number=[]
for p in range(20):
    a=(input("Enter your number here"))
    print(number)
    if a not in number:
        number.append(a)
    print(a)
    
    
    
    

# input_number=int(input("Input the number you want to search here"))
# ab=numbers.count(input_number)
# if ab==1:
#     print(input_number)
# else:
#     print("This number is duplicated")

 

