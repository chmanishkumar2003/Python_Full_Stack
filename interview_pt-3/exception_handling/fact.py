while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input!")
sum=1
for i in range (1,n+1):
    sum*=i
print(sum)
