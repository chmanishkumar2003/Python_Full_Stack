n=1525
sum=0
while n > 0:
    dig=n%10
    print(dig)
    sum=sum+dig
    n=n//10
print("The sum of digits are ",sum)
