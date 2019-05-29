def check(alpha):
    value=""
    if ord(alpha)>=65 and ord(alpha)<=90:
        value="upper case"
    else:
        if ord(alpha)>=97 and ord(alpha)<=122:
            value="lower case"
        else:
            if ord(alpha)>=48 and ord(alpha)<=57:
                value="digits"
            else:
                value="other character"
    return value
alpha=input("enter any character:")
if ord(alpha)>=65 and ord(alpha)<=90:
    print(chr(ord(alpha)+32),alpha)
else:
    if ord(alpha)>=97 and ord(alpha)<=122:
        print(chr(ord(alpha)-32),alpha)
    else:
        if ord(alpha)>=48 and ord(alpha)<=57:
            print("digits")
        else:
            print("other character")

