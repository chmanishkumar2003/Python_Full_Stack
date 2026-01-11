# class NegativeError(Exception):
#     pass

# def pos(n):
#     if n < 0:
#         raise NegativeError("Negative no. are not allowed")
#     else:
#         print("Number is positive")

# try:
#     pos(-5)
# except NegativeError as e:
#     print("Error :",e)

# with open("ans_of-1.txt","w") as file:
#     file.write("Hello,Python!")
# print(file.closed)


#Lambda Function
from functools import reduce

a=[1,2,3,4,5]
sq=set(map(lambda x:x**2,a))
print("Squares of no.s",sq)

even=list(filter(lambda x:x%2==0,a))
print("These are even",even)


fac=reduce(lambda x,y:x*y,a) 
print("Product of list",fac)