n=[1,22,3,4,5]
b=len(n)
max=n[0]
for i in range(b):
    if max < n[i]:
        max=n[i]
print(max)
