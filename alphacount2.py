alpha=[0]*26
msg=input("enter msg:")
i=0
while i<len(msg):
    alpha[ord(msg[i].upper())-65]+=1
    i+=1
i=0
while i<26:
    if alpha[i]>0:
        print(chr(i+65),"=",alpha[i])
    i+=1
