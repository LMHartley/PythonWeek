


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
    print("login closed")
    access="closed"
limit=0
login="no"
while login=="no":
    try: 
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
                login="yes"
            else:
                print("access denied")
    except NameError:
        print("account doesn't exist.")
        print("please enter correct login details.")
    except ValueError:
        print("please enter valid login details")