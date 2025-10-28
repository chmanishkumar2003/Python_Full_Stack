a=[1,2,3,4,5]
n=len(a)
mid=n//2
if n!=0:
    rot_1=a[:mid]
    rot_2=a[mid:]
rotated=rot_2+rot_1
print(rotated)
