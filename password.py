access="no"
limit=0
while access=="no":
    user=input("username:")
    import getpass
    import sys
    p=int(getpass.getpass(stream=sys.stderr))
    import time
    import sys
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if p==5630 and user=="Liam":
        print("access granted")
        access="yes"
    else:
        print("access denied")
        limit=limit+1
    if limit==3:
        access="locked out"
        print("locked out")
