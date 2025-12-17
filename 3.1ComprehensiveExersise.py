
class Car:
    count = 0 

    @staticmethod
    def showHint():
        print("Car 'name' is accessible but immutable")

    def __init__(self, name):
        self._name = name  
        Car.count += 1  
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("Forbidden to modify this attribute!")

    def __del__(self):
        Car.count -= 1  

Car.showHint()
c1=Car("Benz")
print(c1.name)
c1=Car("VM")
print(c1.name)
print(Car.count)
c2=Car("Audi")
print(c1.name)
print(Car.count)
del c1
print(Car.count)
del c2
print(Car.count)