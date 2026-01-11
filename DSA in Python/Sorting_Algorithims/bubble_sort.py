# Bubble sort
# arr=[1,5,2,3,7,4]
# n=len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j+1],arr[j]=arr[j],arr[j+1]
# print(arr)

# Bubble sort using function
def bub(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[1,2,5,3,4,7,6]
print(bub(arr))
