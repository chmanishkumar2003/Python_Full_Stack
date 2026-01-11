# s="Manish"
# rev=""
# for i in s:
#     rev=i+rev
# if rev==s:
#     print("True")
# else:
#     print("False")


# n=[1,2,3,3,3,4]
# for i in n:
#     count=0
#     for j in n:
#         if i == j:
#             count=count+1
#     if count==1:
#      print("The numbers are",i)    

# s={'Name':'Manish'}
# a={'Age':24}
# def add(s,a):
#     return {**s,**a}
# print(add(s,a))
    
    
# m="ManishKumar"
# n=m.lower()
# for i in n:
#     if n.count(i) == 0:
#         continue
#     print(f"{i}:{n.count(i)}")

a=1
b=2
c=3
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
