# Merge Sort 
def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l=arr[:mid]
    r=arr[mid:]
    sl=merge(l)
    sr=merge(r)
    return sort(sl,sr)

def sort(lft,rht):    
    res=[]
    i=j=0
    while i < len(lft) and j < len(rht):
        if lft[i] < rht[j]:
            res.append(lft[i])
            i += 1
        else:
            res.append(rht[j])
            j += 1
    res.extend(lft[i:])
    res.extend(rht[j:])
    return res

arr=[1,4,3,7,5,-12,2]
sarr=merge(arr)
print("Sorted array ",sarr)