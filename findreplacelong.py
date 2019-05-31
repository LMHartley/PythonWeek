find=input("what are you looking for?:")
replace=input("replace with what?:")

f_read=open("hello.txt","r")
f_write=open("hello.txt","w")

for data in f_read:
    i=0
    while i<len(data):
        if data[i]==find[0]:
            if data[i:len(find)+i]==find:
                print(replace,end="",file=f_write)
                i+=len(find)-1
            else:
                print(data[i],end="",file=f_write)
        else:
            print(data[i],end="",file=f_write)
        i+=1
