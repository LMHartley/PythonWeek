file_read=open("hello.txt","r")

find=input("enter find")
replace=input("enter replacement")
for line in file_read:
    for ch in line:
        if ch==find:
            print(replace,end="")
        else:
            print(ch,end="")
