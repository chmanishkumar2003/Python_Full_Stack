# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance+=amount
#             print(f"Deposited money = {amount}.Updated Balance = {self.balance}")
    
#     def withdraw(self,amount):
#         if self.balance < 0:
#             print("Insufficent Funds")
#         elif amount > self.balance:
#             print("Insufficent Funds")
#         else:
#             self.balance -=amount
#             print(f"Withdraw {amount}. New balance = {self.balance}")

#     def check_balance(self):
#         print(f"Current balance:{self.balance}")
#         return self.balance

# account = BankAccount("Manish Kumar", 5000)
# account.check_balance()
# account.deposit(2000)
# account.withdraw(1500)
# account.check_balance()


# class Shape:
#     def area(self):
#         pass
    
# class Rect(Shape):
#     def __init__(self,l,b):
#         self.l=l 
#         self.b= b
#     def area(self):
#         return self.l*self.b

# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r * self.r
    
# rect=Rect(10,15)
# cir=Circle(4)

# print("The area of Rectangle",rect.area())
# print("The area of Circle",cir.area())


# n=4
# class Check:
#     @staticmethod
#     def even(n):
#         if n % 2 == 0:
#             return True
#         else:
#             return False
# print(f"Is {n} is Even ? {Check.even(n)}")


# class Car:
#     count=0

#     def __init__(self,brand):
#         self.brand=brand
#         Car.count += 1

#     def info(self):
#         print(f"Car: {self.brand}")
#     @classmethod
#     def total(cls):
#         print(f"Total cars are {cls.count}")
        
# car1=Car("BMW-300d")
# car2=Car("MS-Shift")
# car3=Car("Range Rover-Chariot")

# car1.info()
# car2.info()
# car3.info()

# Car.total()



def my_decorator(fun):
    def wrapper():
        print("before the function runs")
        fun()
        print("After the function run")
    return wrapper
@my_decorator   #this is the decorator to hello()
def hello():
    print("Helo world!")
hello() 