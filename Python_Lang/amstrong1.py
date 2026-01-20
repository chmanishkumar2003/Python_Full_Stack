n=1531
temp=n
count=0
sum=0
org=n
while n > 0:
    count+=1
    n=n//10
while temp > 0:
    dig=temp%10
    sum+=dig**count
    temp=temp//10
if sum == org:
    print("AMS")
else:
    print("Not AMS")
