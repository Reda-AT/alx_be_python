num1=int(input(("Enter the first number:")))
num2=int(input(("Enter the first number:")))
Op=input("Choose the operation (+, -, *, /)")
if Op=="+":
    R=num1+num2
    print("the result is",R)
elif Op=="-":
    R=num1-num2
    print("the result is",R)
elif Op=="*":
    R=num1*num2
    print("the result is",R)
elif Op=="/":
    if num2==0:
        print("Cannot divide by zero.")
    else:
        R=num1/num2
        print("the result is",R)
