# Selection Sort
# It selects the min element in an array and swaps it to first index.
arr=[4,2,3,6,1,5]
n=len(arr)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if arr[min] > arr[j]:
            min=j                       #Update Minimum value
    arr[i],arr[min]=arr[min],arr[i]     #Swaps the number outside the loop.
print(arr)
