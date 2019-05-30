login="no"
while login=="no" or login=="exit":
    print("************MAIN MENU**************")
    choice = input("""
        A: Login
        B: Create account
        C: Exit application

        Please enter your choice: """)
    if choice == "A" or choice =="a":
        login="no"
        while login=="no":
            try: 
                access="no"
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
                    if p==setp and user==setuser:
                        print("access granted")
                        access="yes"
                        login="yes"
                    else:
                        print("access denied")
            except NameError:
                print("account doesn't exist.")
                tryagain=input("would you like to try again?:")
                if tryagain=="no":
                    login="exit"

            except ValueError:
                print("please enter valid login details")
    elif choice == "B" or choice =="b":
        setuser=input("enter new username:")
        import getpass
        import sys
        setp=int(getpass.getpass(stream=sys.stderr))
        import time
        import sys
        animation = "|/-\\"
        for i in range(10):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("account created.")
    elif choice=="C" or choice=="c":
        print("    menu exited")
        login="exited"
    else:
        print("You must only select either A,B or C.")
        print("Please try again")
    while login=="yes" and access=="yes":
        print("************FUNCTION MENU**************")
        choice = input("""
                A: Word Reverse
                B: Word Replce
                C: Duplicate Words
                D: Word Count
                E: Logout

                Please enter your choice: """)
        if choice == "A" or choice =="a":
            def reverse_string1(s):
                """Return a reversed copy of `msg`"""
                return s[::-1]
            msg=input("enter msg:")
            smsg=msg.split(" ")
            word=""
            for x in smsg:
                rword=reverse_string1(x)
                word+=rword+" "
            print(word)
        if choice == "B" or choice =="b":
            msg=input("enter msg:")
            find=input("enter find:")
            rep=input("enter replacement:")
            print(msg.replace(find,rep))
        if choice == "C" or choice =="c":
            def unique_list(l):
                ulist = []
                [ulist.append(x) for x in l if x not in ulist]
                return ulist
            a=input("enter text here:")
            a=' '.join(unique_list(a.split()))
            print(a)
        if choice == "D" or choice =="d":
            msg=input("enter msg here:")
            def wordcount(msg):
                word=0
                i=0
                while i<len(msg):
                    if msg[i]==" ":
                        word+=1
                    i+=1
                return word+1
            print("word count:",wordcount(msg))
        if choice == "E" or choice =="e":
            print("            logged out")
            login="exit"
