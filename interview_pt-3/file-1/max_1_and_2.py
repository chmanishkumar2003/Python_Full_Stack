lst=[1,5,6,3,7,2]
n=len(lst)
max1=lst[0]
for i in range(1,n):
    if lst[i] > max1 :
        max1=lst[i]

max2=lst[0]
if max1==max2:
    max2=lst[1]

for i in range(n):
    if lst[i]!=max1 and lst[i]>max2:
        max2=lst[i]

print("Secound Max in list is",max2)
print("Max value in list is",max1)
