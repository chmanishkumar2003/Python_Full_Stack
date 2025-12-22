while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input!")
if n==1 or n==0:
    print(f"{n} is not a prime or composite number")
else:
    count=0
    for i in range(2,n):
        if n % i == 0:
            count=count+1
    if count > 0:
        print(f"{n} is not a prime")
    else:
        print(f"{n} is a prime no.")

