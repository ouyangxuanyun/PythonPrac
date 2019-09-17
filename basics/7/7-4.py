"""
7-4 创建可管理的对象属性（访问器，数据器）
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return round(self.radius, 1)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('Wrong Type')
        self.radius = radius

    # def get_area(self):
    #     return self.radius ** 2 * math.pi
    #
    # def set_area(self, s):
    #     self.radius = math.sqrt(s / math.pi)

    @property
    def S(self):
        return self.radius ** 2 * math.pi

    @S.setter
    def S(self, s):
        self.radius = math.sqrt(s / math.pi)

    R = property(get_radius, set_radius)


c = Circle(5.712)
# print(c.get_radius())

c.S = 99.88
print(c.S)
print(c.R)