# Linear Search
# n=[1,2,3,4,5]
# tar=3
# for i in range(len(n)):
#     if n[i]==tar:
#         print("Target Found at index",i)
#         break
# else:
#     print("Target Not found  in list")

# Linear search using function
def is_lin(n,tar):
    for i in range(len(n)):
        if n[i]==tar:
            return i
    return -1

n=[1,2,3,4]
tar=3
res=is_lin(n,tar)
if res!= -1:
    print("Target found at index",res)
else:
    print("Target not in List")