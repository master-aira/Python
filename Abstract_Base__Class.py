from abc import ABCMeta,abstractmethod
class shape(metaclass = ABCMeta):
    @abstractmethod  #Iska Matlab sabka def krna hai
    def print_area(self):
        return 0
class Rectangle(shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 10
    def print_area(self):
        return self.length * self.breadth
rect1 = Rectangle()
# print(rect1.print_area)