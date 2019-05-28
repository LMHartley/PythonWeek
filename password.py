user=input("username:")
import getpass
import sys
p=getpass.getpass(stream=sys.stderr)

import time
import sys
animation = "|/-\\"
for i in range(10):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("                       ")

if p == 5630:
    print("yes")


