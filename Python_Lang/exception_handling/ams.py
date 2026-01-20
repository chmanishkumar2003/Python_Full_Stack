while True:
    try:
        n = int(input("Enter a number: "))
        break                      # exit loop if input is correct
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
total = 0
temp = n
digits = len(str(n))
while temp > 0:
    dig = temp % 10
    total = total + dig ** digits
    temp = temp // 10
if total == n:
    print("It is an Armstrong number")
else:
    print("Not an Armstrong number")
