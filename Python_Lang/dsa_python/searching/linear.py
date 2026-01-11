arr=[1,2,3,4,5]
n=len(arr)
tar=3

#Checking number in array using for loop
for i in range(n):
    if tar==arr[i]:
        print(f"Target found at index {i}")
        break
else:
    print("Target not found")