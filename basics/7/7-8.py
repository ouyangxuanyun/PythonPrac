# Time : 2019/9/22 19:54
# Author : Fu
# Software: PyCharm

"""
7-8 通过实例方法名字的字符串调用方法
"""
from operator import methodcaller


class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def get_area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def getArea(self):
        return self.a * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.141592657


def get_area(shape, method_name=['area', 'get_area', 'getArea']):
    for name in method_name:
        f = getattr(shape, name, None)  # None 表示如果没有这个属性返回None，而不报错
        if f:
            return f()

        # # 或者使用methodcaller
        # s = 'abcqweradf'
        # s.find('abc',3)
        # methodcaller('find', 'abc',3)(s)

        # if hasattr(shape,name):
        #     return methodcaller(name)(shape)


shape1 = Circle(1)
shape2 = Triangle(5, 3, 4)
shape3 = Rectangle(4, 6)

shape_list = [shape1, shape2, shape3]

area_list = list(map(get_area, shape_list))
print(area_list)
