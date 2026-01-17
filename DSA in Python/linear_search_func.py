def is_lin(n,tar):
    for i in range(len(n)):
        if n[i]==tar:
            return i
    return -1

n=[1,2,3,4]
tar=3
res=is_lin(n,tar)
if res!= -1:
    print("Target found at index",res)
else:
    print("Target not in List")
