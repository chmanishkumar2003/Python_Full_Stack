class Shape:
    def area(self):
        pass
    
class Rect(Shape):
    def __init__(self,l,b):
        self.l=l 
        self.b= b
    def area(self):
        return self.l*self.b

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r * self.r
    
rect=Rect(10,15)
cir=Circle(4)

print("The area of Rectangle",rect.area())
print("The area of Circle",cir.area())
