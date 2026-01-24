# Counting Frequency of element without using sort
n=[1,2,2,4,3,5,3,3]
unq=[]
count=[]
for i in n:
    if i not in unq:
        unq.append(i)
        count.append(1)
    else:
        idx=unq.index(i)
        count[idx] += 1
for i in range(len(unq)):
    print(unq[i],":",count[i])
