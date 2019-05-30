def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
a=input("enter text here:")
a=' '.join(unique_list(a.split()))
print(a)