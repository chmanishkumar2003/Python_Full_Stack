# Insertion Sort
arr=[1,4,3,2,5,8]
n=len(arr)
for i in range(n):
    key=arr[i]
    pos=i
    for j in range(i-1,-1,-1):
        if arr[j]> key:
            arr[j+1]=arr[j]         #shift
            pos=j
        else:
            break
    arr[pos]=key
print(arr)
