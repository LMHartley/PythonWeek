def tax(salary):
    if salary>2000:
        t=salary*21/100
    else:
        t=salary*15/100
    return t
salary1=int(input("enter your salary:"))
print("----------------------------------------------")
print("your annual NET pay is:",int(salary1-tax(salary1)))
print("your monthly NET pay is:",int((salary1-tax(salary1))/12))
