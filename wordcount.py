msg=input("enter msg here:")
def wordcount(msg):
    word=0
    i=0
    while i<len(msg):
        if msg[i]==" ":
            word+=1
        i+=1
    return word+1
print("word count:",wordcount(msg))