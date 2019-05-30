def reverse_string1(s):
    """Return a reversed copy of `msg`"""
    return s[::-1]
msg=input("enter msg:")
smsg=msg.split(" ")
word=""
for x in smsg:
    rword=reverse_string1(x)
    word+=rword+" "
print(word)