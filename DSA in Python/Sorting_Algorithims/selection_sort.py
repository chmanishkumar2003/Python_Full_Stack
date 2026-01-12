# Selection Sort using Function
def sel(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j                              #Updates min and exits j loop.
        arr[i],arr[min]=arr[min],arr[i]            #Swaps the number outside the loop with correct index.
    return arr
arr=[1,3,5,4,2,7]
print(sel(arr))
