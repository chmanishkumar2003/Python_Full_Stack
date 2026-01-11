numbers=[1,2,3]      #here numbers are iterable
item=iter(numbers)   #here item is an iterator
print(next(item))  #1
print(next(item))  #2  
print(next(item))  #3  
print(next(item)) #Stop iteration