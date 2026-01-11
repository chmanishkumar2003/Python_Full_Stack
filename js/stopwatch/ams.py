# while True:
#     try:
#         n = int(input("Enter a number: "))
#         break                      # exit loop if input is correct
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")
# total = 0
# temp = n
# digits = len(str(n))
# while temp > 0:
#     dig = temp % 10
#     total = total + dig ** digits
#     temp = temp // 10
# if total == n:
#     print("It is an Armstrong number")
# else:
#     print("Not an Armstrong number")


# while True:
#     try:
#         n = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Invalid input!")
# if n==1 or n==0:
#     print(f"{n} is not a prime or composite number")
# else:
#     count=0
#     for i in range(2,n):
#         if n % i == 0:
#             count=count+1
#     if count > 0:
#         print(f"{n} is not a prime")
#     else:
#         print(f"{n} is a prime no.")

# while True:
#     try:
#         n = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Invalid input!")
# sum=1
# for i in range (1,n+1):
#     sum*=i
# print(sum)

# n=1525
# sum=0
# while n > 0:
#     dig=n%10            #To extract last digit of number
#     print(dig)
#     sum=sum+dig          
#     n=n//10             #To remove last digit of the number
# print("The sum of digits are ",sum)

# n=1531
# temp=n
# count=0
# sum=0
# org=n
# while n > 0:
#     count+=1
#     n=n//10
# while temp > 0:
#     dig=temp%10
#     sum+=dig**count
#     temp=temp//10
# if sum == org:
#     print("AMS")
# else:
#     print("Not AMS")

# n=100000
# for i in range(10,n):
#     count=len(str(i))
#     temp=i
#     sum=0
#     while temp > 0:
#         digit=temp%10
#         sum=sum+digit**count
#         temp=temp//10
#     if sum==i:
#         print(i," is AMS")
    
# n=50
# for i in range(2,n):
#     count=0
#     for a in range(2,i):
#         if i % a == 0:
#             count=count+1
#             break
#     if count ==0:
#         print(i,"It is prime no.") 

# def is_ams(n):
#     temp=n
#     count=len(str(n))
#     sum=0
#     while temp > 0:
#         dig=temp%10
#         sum=sum+dig**count
#         temp=temp//10
#     return sum==n
# while True:   
#     try:
#         n=int(input("Enter a no.: "))
#         if n < 0 :
#             print("Not ams")
#         elif is_ams(n):
#             print("Amstrong no.")
#         else:
#             print("Not ams")
#         break
#     except ValueError:
#         print("Invalid output")

# n=121
# temp=n
# rev=0
# while temp > 0:
#     d=temp % 10
#     rev=rev*10+d
#     temp=temp//10
# if n==rev:
#     print("Same")
# else:
#     print("NS")

# Max of 3 using Ternary operator
# a=222
# b=31
# c=5
# res="C is max" if c>a and c>b else ("B is max" if b>a and b>c else "A is max")
# print(res)

# Recursive Functions
# Factorial
# n=5
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(n))

# def is_prime(n, i=2):
#     if n <= 1:
#         return False
#     if i * i > n:
#         return True
#     if n % i == 0:
#         return False
#     return is_prime(n, i + 1)

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("Prime number")
# else:
#     print("Not a prime number")

# n=[1,2,3,4,5]
# sum=0
# for i in n:
#     sum=sum+i
# print(sum)

# n=[1,22,3,4,5]
# b=len(n)
# max=n[0]
# for i in range(b):
#     if max < n[i]:
#         max=n[i]
# print(max)

# n=[1,2,3,4,5]
# b=len(n) - 1
# rev=[]
# while b >= 0:
#     rev.append(n[b])
#     b -= 1
# print(rev)

# Removing duplicates from list using set.
# n=[1,2,3,2,3,4]
# unq=list(set(n))
# print(unq)

# Removing duplicates from list without using set.
# n=[1,2,3,4,2,3]
# unq=[]
# for i in n:
#     if i not in unq:
#         unq.append(i)
# print("Unique Variables =",unq)

#Printing duplicates, unique elements from list .
# n = [1,2,3,2,3,4]
# unique = []
# repeated = []
# for i in n:
#     if i not in unique:
#         unique.append(i)
#     elif i not in repeated:
#         repeated.append(i)
# print("Unique =", unique)
# print("Repeated =", repeated)

# Counting Frequency of element using sort
# n=[1,2,2,3,3,4]
# count=1
# n.sort()
# for i in range(len(n)-1):
#     if n[i]==n[i+1]:
#         count += 1
#     else:
#         print(n[i],":",count)
#         count=1
# print(n[-1],":",count)

# Counting Frequency of element without using sort
# n=[1,2,2,4,3,5,3,3]
# unq=[]
# count=[]
# for i in n:
#     if i not in unq:
#         unq.append(i)
#         count.append(1)
#     else:
#         idx=unq.index(i)
#         count[idx] += 1
# for i in range(len(unq)):
#     print(unq[i],":",count[i])

# Built-in Functions in python
# n=[10,20,30,40]
# print(len(n))           #For length of array
# print(sum(n))           #For Sum of array
# print("Min:",min(n),"Max:",max(n))    #For min and max in an array
# # Enumerate function which gives index and value together
# for a,b in enumerate(n):
#     print(a,b) 

# s="Manish"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# Functions 
# def revs(s):
#     rev=""
#     for i in s:
#         rev=i+rev
#     return rev
# s="Manish"
# print(revs(s))

# def max(n):
#     a=n[0]
#     for i in range(len(n)):
#         if n[i] > a:
#             a=n[i]
#     return a
# n=[10,20,3,4]
# print(max(n))

# def count(s):
#     count=0
#     for i in s:
#         if i in "AEIOUaeiou":
#             count=count+1
#             print("Vowels are ",i)
#     return count
# s="Akash"
# print("And count of Vowels are",count(s))

# def ams(n):
#     for i in range(10,n):
#         count=len(str(i))
#         temp=i
#         sum=0
#         while temp > 0:
#             dig=temp%10
#             sum=sum+dig**count
#             temp=temp//10
#         if sum==i:
#             print("Ams",i)
#     return sum
# n=1000
# ams(n)

# def prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         print(f"Factor of {n} is {i}" )
#         if n % i == 0:
#             return False
#     return True
# n=24
# print(prime(n))

# Counting swaps
arr=[1,4,2,3]
temp=sorted(arr)
pos={}
for i in range(len(arr)):
    pos[arr[i]]=i
swaps=0
for i in range(len(arr)):
    if temp[i]!=arr[i]:
        idx=pos[temp[i]]