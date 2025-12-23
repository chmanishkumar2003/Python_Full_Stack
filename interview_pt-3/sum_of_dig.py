n=1525
sum=0
while n > 0:
    dig=n%10            #To extract last digit of number
    print(dig)
    sum=sum+dig          
    n=n//10             #To remove last digit of the number
print("The sum of digits are ",sum)
