

# Insertion Sort using Function
def ins(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        pos=i
        for j in range(i-1,-1,-1):
            if arr[j]>key:
                arr[j+1]=arr[j]
                pos=j            
            else:
                break
        arr[pos]=key
    return arr

arr=[1,4,2,5,3,6]
print(ins(arr))
