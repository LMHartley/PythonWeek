name=input("enter name here:")
salary=int(input("enter salary here:"))
if salary>2000:
    tax=salary*15/100
else:
    tax=salary*21/100
net=salary-tax
print("-----------------------------")
print("Your net salary is:",net)
print("-----------------------------")
