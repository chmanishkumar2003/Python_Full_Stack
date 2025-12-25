n=100000
for i in range(10,n):
    count=len(str(i))
    temp=i
    sum=0
#Temp is used to store orginal number.
    while temp > 0:
        digit=temp%10
        sum=sum+digit**count
        temp=temp//10
    if sum==i:
        print(i," is AMS")
    
