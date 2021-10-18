"""Surcharge de méthode"""
from abc import ABC

class Shape(ABC):
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
    
    def area(self):
        return self.lenght * self.lenght
