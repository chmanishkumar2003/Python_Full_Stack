def ams(n):
    for i in range(10,n):
        count=len(str(i))
        temp=i
        sum=0
        while temp > 0:
            dig=temp%10
            sum=sum+dig**count
            temp=temp//10
        if sum==i:
            print("Ams",i)
    return sum
n=1000
ams(n)
