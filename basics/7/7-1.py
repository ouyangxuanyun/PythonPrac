# Time : 2019/9/16 22:36
# Author : Fu
# Software: PyCharm
"""
7-1 派生内置不可变类型并修改实例
"""


# 自定义一种新类型的元组，对于传入的可迭代对象，只保留int类型且值大于0的元素
class IntTuple(tuple):
    def __new__(cls, iterable):
        f_it = (e for e in iterable if isinstance(e, int) and e > 0)
        return super().__new__(cls, f_it)


int_t = IntTuple((1, -1, 'abc', 6, ['x', 1, 2], 3))
print(int_t)
