# Binary Search using function
def bin(n,tar):
    arr=sorted(n)
    left=0
    right=len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid] > tar:
            right=mid-1
        else:
            left=mid+1
    return -1
n=[1,2,6,3,7,4,5]
tar=5
res=bin(n,tar)
if res != -1:
    print("Target found at index",res)
else:
    print("Target not in list")
