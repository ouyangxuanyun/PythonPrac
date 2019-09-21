# Time : 2019/9/21 21:59
# Author : Fu
# Software: PyCharm

"""
7-5 让类支持比较操作
"""

# 基础方法
from abc import ABCMeta, abstractmethod
from functools import total_ordering
import math


# 使用total_ordering简化比较过程，只要实现__eq__ 和__lt__或者__gt__中的一个即可
@total_ordering
class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return 'Rect:(%s, %s)' % (self.w, self.h)

    def __lt__(self, other):
        print('__lt__', self, other)
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


rect1 = Rect(10, 10)
rect2 = Rect(9, 9)
print(rect1 > rect2)


# 进阶：可以实现一个抽象类，把比较函数放入抽象类中，这样继承抽象类的类相互间都可以进行比较

@total_ordering
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        print('__lt__', self, other)
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi


class Square(Shape):
    def __init__(self, l):
        self.l = l

    def area(self):
        return self.l ** 2


c1 = Circle(10)
c2 = Circle(9)
s = Square(10)
print(c1 > c2)
print(c1 > s)
