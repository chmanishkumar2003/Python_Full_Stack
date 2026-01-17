# Linear Search
n=[1,2,3,4,5]
tar=3
for i in range(len(n)):
    if n[i]==tar:
        print("Target Found at index",i)
        break
else:
    print("Target Not found  in list")

