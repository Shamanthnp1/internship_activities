num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation=input("enter the operation (+, -, *, /):")
if operation=='+':
    result=num1+num2
    print("The result is:", result)
elif operation=='-':
    result=num1-num2
    print("The result is:", result)
elif operation=='*':
    result=num1*num2
    print("The result is:", result)
elif operation=='/':
    if num2!=0:
        result=num1/num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
    