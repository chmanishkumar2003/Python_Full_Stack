# n=[1,2,3,4]
# rev=[]
# for i in n:
#     rev=[i]+rev
# print(rev)


# a=[[1,2],[3,4]]
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)
# print(b)


# a="ManishKumar"
# n=len(a)
# count=0
# vowels="aeiouAEIOU"
# for i in a:
#     if i in vowels:
#         count=count+1
# print("The string contains vowels",count)
# const=n-count
# print("The string contains consonants",const)

    
# n=[5,4,1,2,3,4,4,6,3]
# b=list(set(n))
# print(b)
# max_2=b[-2]
# print(max_2)


a=[1,2,3,4,5]
n=len(a)
mid=n//2
if n!=0:
    rot_1=a[:mid]
    rot_2=a[mid:]
rotated=rot_2+rot_1
print(rotated)