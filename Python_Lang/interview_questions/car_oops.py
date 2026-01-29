class Car:
    count=0

    def __init__(self,brand):
        self.brand=brand
        Car.count += 1

    def info(self):
        print(f"Car: {self.brand}")
    @classmethod
    def total(cls):
        print(f"Total cars are {cls.count}")
        
car1=Car("BMW-300d")
car2=Car("MS-Shift")
car3=Car("Range Rover-Chariot")

car1.info()
car2.info()
car3.info()

Car.total()
