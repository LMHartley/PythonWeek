numbers=[]
while True:
    num=int(input("enter number:"))
    if num==0:
        break
    else:
        numbers.append(num)
highest=numbers[0]
i=1
while i<len(numbers):
    if numbers[i]>highest:
        highest=numbers[i]
    i+=1
print("highest number is ",highest)


