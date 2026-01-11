# Binary Search
n=[1,2,5,3,6,4,8,9]
tar=6
arr=sorted(n)
left=0
right=len(arr)-1
while left <= right:
    mid=(left+right)//2
    if arr[mid]==tar:
        print("Target Found at index",mid)
        break
    elif n[mid] < tar:
        left=mid+1
    else:
        right=mid-1
else:
    print("Target value not in the list")

