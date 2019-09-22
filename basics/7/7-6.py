# Time : 2019/9/22 10:33
# Author : Fu
# Software: PyCharm

"""
7-6 对实例属性进行类型检查
"""


# 使用描述符来实现需要类型检查的属性， 分别实现__get__,__set__,__delete__方法， 在__set__ 内做类型检查

class Attr:
    def __init__(self, key, type_):
        self.key = key
        self.type_ = type_

    def __set__(self, instance, value):
        print('in __set__')
        if not isinstance(value, self.type_):
            raise TypeError('must be %s' % self.type_)
        instance.__dict__[self.key] = value

    def __get__(self, instance, owner):
        print('in __get__')
        return instance.__dict__[self.key]

    def __delete__(self, instance):
        print('in __delete__')
        del instance.__dict__[self.key]


class Person:
    name = Attr('name', str)
    age = Attr('age', int)


p = Person()
p.name = 'fu'
p.age = '3'
