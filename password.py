user=input("enter username:")
import getpass
getpass.getpass("enter password:")
import time
import sys


animation = "|/-\\"

for i in range(10):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("                       ")
if getpass==5630 and user=="Liam":
    print("--------------------")
    print("access granted")
    print("--------------------")
if getpass!=5630 and user!="Liam":
    print("--------------------")
    print("access denied")
    print("--------------------")
if getpass==5630 and user!="Liam":
    print("--------------------")
    print("access denied")
    print("--------------------")
if getpass!=5630 and user=="Liam":
    print("--------------------")
    print("access denied")
    print("--------------------")