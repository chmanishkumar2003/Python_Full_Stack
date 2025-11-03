lst=[1,2,2,3,4,5,5,6,7]
def dif(lst):
    unq=[]
    for i in lst:
        if i not in unq:
            unq.append(i)
    return unq

print("Original list",lst)
print("Unq list",dif(lst))
