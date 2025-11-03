n=113
def sum(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n%10) + sum(n//10)
print(sum(n))
