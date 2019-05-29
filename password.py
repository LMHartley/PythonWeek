acc=input("do you have an account?:")
if acc=="yes":
    access="no"
else:
    setuser=input("enter new username:")
    import getpass
    import sys
    setp=int(getpass.getpass(stream=sys.stderr))
    print("account created.")
login=input("would you like to login?:")
if login=="yes":
    access="no"
else:
    access="closed"
limit=0
while access=="no" and limit<3:
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
    if p==setp and user==setuser:
        print("access granted")
        access="yes"
    else:
        print("access denied")
        limit=limit+1
        if limit==3:
            access="locked out"
            print("locked out")
