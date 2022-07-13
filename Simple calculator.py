
                                                # SIMPLE CALCULATOR


n1 = float(input("Enter the 1st Number : "))
n2 = float(input("Enter the 2nd Number : "))

operation = input("Enter the Operation you want to perform (+,-,*,/,%, ^) : ")

if operation == '+':
    print(n1, "+", n2, "=", n1+n2)
elif operation == '-':
    print(n1, "-", n2, "=", n1-n2)
elif operation == '*':
    print(n1, operation, n2, "=", n1*n2)
elif operation == '/':
    print(n1, operation, n2, "=", n1/n2)
elif operation == '%':
    print(n1, operation, n2, "=", n1%n2)
elif operation == '^':
    print(n1, operation, n2, "=", n1**n2)
else:
    print("!!!INVALID OPERATION!!!")
