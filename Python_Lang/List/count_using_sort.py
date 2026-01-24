# Counting Frequency of element using sort
n=[1,2,2,3,3,4]
count=1
n.sort()
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count += 1
    else:
        print(n[i],":",count)
        count=1
print(n[-1],":",count)
