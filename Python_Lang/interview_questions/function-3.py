# n=6
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
# print(sum)

# n=6
# def fact(n):
#     if n == 0  or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(n))


# def fib(n):
#     if n ==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return fib(n-1) + fib(n-2)

# n=6
# for i in range(n):
#     print(fib(i),end=" ")


# n=113
# def sum(n):
#     if n ==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (n%10) + sum(n//10)
# print(sum(n))

lst=[1,2,2,3,4,5,5,6,7]
def dif(lst):
    unq=[]
    for i in lst:
        if i not in unq:
            unq.append(i)
    return unq

print("Original list",lst)
print("Unq list",dif(lst))
