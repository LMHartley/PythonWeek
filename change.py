cost=int(input("Enter Cost:"))
paid=int(input("Enter money given:"))
change=paid-cost
n50=0
n20=0
n10=0
n5=0
n2=0
n1=0
if change>=50:
    n50= int(change/50)
    print("£50:",n50)
    change=change-(n50*50)
if change>=20:
    n20=int((change/20))
    print("£20:",n20)
    change=change-(n20*20)
if change>=10:
    n10=int((change/10))
    print("£10:",n10)
    change=change-(n10*10)
if change>=5:
    n5=int((change/5))
    print("£5:",n5)
    change=change-(n5*5)
if change>=2:
    n2=int((change/2))
    print("£2:",n2)
    change=change-(n2*2)
if change>=1:
    n1=int((change/1))
    print("£1:",n1)
    change=change-(n1*1)