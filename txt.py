file_read=open("hello.txt","r")

for line in file_read:
    for ch in line:
        if ch=="o":
            print("*",end="")
        else:
            print(ch,end="")
