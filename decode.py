msg=input("enter msg here:")
def change(msg)
    i=0
    value=""
    while i<len(msg):
        msgi=ord(msg[i])
        if msgi>=65 and msgi<=90:
            value+=chr(msgi+32)
        else:
            if msgi>=97 and msgi<=122:
                value+=chr(msgi-32)
            else:
                if msgi>=48 and msgi<=57:
                    value+=str(int(chr(msgi))*2)
                else:
                    value+="*"
        i=i+1
    return value
print(value)