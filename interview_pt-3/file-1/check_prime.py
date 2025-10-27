n=29
count=0
for i in range(2,n+1):
    if n%i == 0:
        count +=1
if count > 1:
    print(f"{n} is not prime number")
else:
    print(f"{n} is prime number")
