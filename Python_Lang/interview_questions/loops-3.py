# n=6
# a=0    
# b=1
# for i in range(n):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c


# n=8
# for i in range(1,11):
#     print(f"{n} x {i} = {i*n}")


# n=20
# for i in range(2,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)
    

# n=100
# for i in range(1,n+1):
#     if i % 3 ==0 and i % 5 ==0:
#         print(i)




# def anagram(st_1,st_2):
    
#     if len(st_1)!=len(st_2):
#         print("Not Ana")
#     else :
#         for i in st_1:
#             if st_1.count(i)!=st_2.count(i):
#                 print("Not Ana")
#         print("Anagram")

# print(anagram("race","cared"))


# tup=(1,2,3)
# print(tup[2])
# tup[0]=50
# print(tup[0])


# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# APPEND
# lst=[1,2,3]
# lst.append(4)
# print(lst)

# #EXTEND
# lst.extend("abc")
# lst.extend([1,2])
# print(lst)


# n=29
# count=0
# for i in range(2,n+1):
#     if n%i == 0:
#         count +=1
# if count > 1:
#     print(f"{n} is not prime number")
# else:
#     print(f"{n} is prime number")


# lst=[1,5,6,3,7,2]
# n=len(lst)
# max1=lst[0]
# for i in range(1,n):
#     if lst[i] > max1 :
#         max1=lst[i]

# max2=lst[0]
# if max1==max2:
#     max2=lst[1]

# for i in range(n):
#     if lst[i]!=max1 and lst[i]>max2:
#         max2=lst[i]

# print("Secound Max in list is",max2)
# print("Max value in list is",max1)


