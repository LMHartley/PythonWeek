count=0
again=input("would you like to search?:")
s=1
while s==1:
    while again=="yes":
        msg=input("enter message here:")
        char=input("what character are you looking for?:")
        i=0
        while i<=len(msg)-1:
            if msg[i]==char:
                count=count+1
            i=i+1
        print(char,"appears",count,"time(s).")
        again=input("would you like to search again?:")
        count=0
    if again=="no":
        print("thanks for searching!")
        s=2
    else:
        print("invalid response")
        again=input("would you like to search again?:")
