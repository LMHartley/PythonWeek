f=0
msg=input("enter msg:")
find=input("enter find:")
i=0
while i<len(msg):
    if msg[i]==find[0]:
        if msg[i:len(find)+i]==find:
            f=f+1
            i=i+len(find)-1
    i=i+1
print("count of",find,":",f)