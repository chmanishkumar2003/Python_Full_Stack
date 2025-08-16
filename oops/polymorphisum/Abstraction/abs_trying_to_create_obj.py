from abc import ABC,abstractmethod

#Class Animal is an abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass    #Abstract method, must be implemented by subclasses

#Typing to create object of an abstract class will raise an error    
try:
    a=Animal()
except TypeError as e:
    print(f"Error: {e}")
    
#subclass Dog inherits from Animal and implements the sound method
class Dog(Animal):
    def sound(self):
        return "Woof"
    
d=Dog()
print(d.sound())  
    