n=[7,8,1,3,2,4,6,5]
for i in range(1, len(n)):
    min = n[i]
    j = i - 1
    while j >= 0 and min < n[j]:
        n[j + 1] = n[j]
        j -= 1
    n[j + 1] = min
print(n)