# This is program that will read a five digit number from right to left and vice versal
# and the number will be same. if they are same, the program will state Palindrome.

num=int(input("Enter a five digit number here:" ))
string=str(num)
rev_string=string[::-1]
print("The reverse string is:, rev_string ")
if string==rev_string:
    print("This is a palindrone")
else:
    print('This is not a palindrone')


            
            





