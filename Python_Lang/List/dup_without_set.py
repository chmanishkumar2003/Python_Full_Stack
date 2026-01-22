# Removing duplicates from list without using set.
n=[1,2,3,4,2,3]
unq=[]
for i in n:
    if i not in unq:
        unq.append(i)
print("Unique Variables =",unq)
