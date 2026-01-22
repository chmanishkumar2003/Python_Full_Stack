#Printing duplicates, unique elements from list .
n = [1,2,3,2,3,4]
unique = []
repeated = []
for i in n:
    if i not in unique:
        unique.append(i)
    elif i not in repeated:
        repeated.append(i)
print("Unique =", unique)
print("Repeated =", repeated)
