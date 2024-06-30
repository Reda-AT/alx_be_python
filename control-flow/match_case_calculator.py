num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
Op=input("Choose the operation (+, -, *, /):")
match Op:
    case "+":
        R=num1+num2
        print("the result is",R)
    case "-":
        R=num1-num2
        print("the result is",R)
    case "*":
        R=num1*num2
        print("the result is",R)
    case "/":
        if num2==0:
            print("Cannot divide by zero.")
        else:
            R=num1/num2
            print("the result is",R)