def addition(a,b):
    c=a+b
    print("result is:",c)
def subtraction(a,b):
    c=a-b
    print("result is:",c)
def multiply(a,b):
    c=a*b
    print("result is:",c)
def divide(a,b):
    c=a/b
    print("result is:",c)
def operation(f,a,b):
    f(a,b)
use="y"
while use=="y":
    num1=int(input("enter number 1:"))
    func=input("+,-,x or /?:")
    if func=="+":
        func=addition
    elif func=="-":
        func=subtraction
    elif func=="x":
        func=multiply
    elif func=="/":
        func=divide
    else:
        print("invalid response")
    num2=int(input("enter number 2:"))
    operation(func,num1,num2)
    use=input("would you like to continue?:")