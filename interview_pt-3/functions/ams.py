def is_ams(n):
    temp=n
    count=len(str(n))
    sum=0
    while temp > 0:
        dig=temp%10
        sum=sum+dig**count
        temp=temp//10
    return sum==n
while True:   
    try:
        n=int(input("Enter a no.: "))
        if n < 0 :
            print("Not ams")
        elif is_ams(n):
            print("Amstrong no.")
        else:
            print("Not ams")
        break
    except ValueError:
        print("Invalid output")
