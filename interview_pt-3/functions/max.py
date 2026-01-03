def max(n):
    a=n[0]
    for i in range(len(n)):
        if n[i] > a:
            a=n[i]
    return a
n=[10,20,3,4]
print(max(n))
