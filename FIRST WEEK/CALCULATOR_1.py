print("This programme does all your Arethmetic calculation which involves addition,multiplication,subtraction,division and exponetials")
print("Rule 1: represent addition sign with: +")
print("Rule 2: represent multiplication sign with: *")
print("Rule 3: represent division sign with: /")
print("Rule 4: represesnt subtraction sign with: -")
print("Rule 5: represent exponential sign with: **")
integer_1=int(input("Put your first number here"))
integer_2=int(input('Put your second number here'))
operator=input("Put the sign here")
if operator == '+':
    print(integer_1+integer_2)
if operator == '*':
    print(integer_1*integer_2)
if operator == "-":
    print(integer_1-integer_2)
if operator == '**':
    print(integer_1**integer_2)
if operator == '/':
    print(integer_1/integer_2)
   
