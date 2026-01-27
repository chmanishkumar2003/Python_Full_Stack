# Function for checking weather thenumber is prime or not.
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        print(f"Factor of {n} is {i}" )
        if n % i == 0:
            return False
    return True
n=24
print(prime(n))
