arr=[1,2,3,4,5]
n=len(arr)
tar=3

left=0
right=n-1


#while loop for countinous check
while left<=right:
    mid=(right+left) // 2
    
    if arr[mid]==tar:
        print(f"Tagrt found at index {mid} ")
        break
    if arr[mid]<tar:
        right=mid+1
    else:
        left=mid-1
        
else:
    print("Target not found")