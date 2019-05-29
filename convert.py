ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
num=int(input("enter number here:"))
answer=""
if num>=1000 and num<=9999:
    answer+=ones[int(num/1000)]+"thousand "
    num%=1000
if num>=100 and num<=999:
    answer+=ones[int(num/100)]+"hundred "
    num%=100
if num>=20 and num<=99:
    answer+=tens[int(num/10)]
    num%=10
if num>=1 and num<=9:
    answer+=ones[int(num)]
print(answer)