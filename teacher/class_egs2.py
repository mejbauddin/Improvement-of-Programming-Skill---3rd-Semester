class Circle_:
    def __init__(self, radius):
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
 
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius can not be negative")
        self._radius = value
 
    @radius.deleter
    def radius(self):
        del self._radius

class ClsCount:
    count = 0
    def __init__(self):
        ClsCount.count += 1
    @classmethod
    def get_count(cls):
        print(f"{cls.count} objects are implemented.")

class MoneyCalc:
    @staticmethod
    def calc_discount(price, discount_rate):
        return price * (1 - discount_rate)
    @staticmethod
    def cvt_currency(amount, exchange_rate):
        return amount * exchange_rate

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        """calculate the area of the shape"""
        pass
    @abstractmethod
    def perimeter(self):
        """calculate the perimeter of the shape"""
        pass
