# Time : 2019/8/4 22:07
# Author : Fu
# Software: PyCharm

from collections import Iterable


class PrimeNumbers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))


pn = PrimeNumbers(1, 30)
for n in pn:
    print(n)



'''
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

元素除了是 0、空、None、False 外都算 True。

'''

'''
map() 会根据提供的函数对指定序列做映射。
map(function, iterable, ...)

Python 2.x 返回列表。
Python 3.x 返回迭代器。
map(lambda x, y: x+y,[1,3,5,7,9],[2,4,6,8,10])

结果：
[3,7,11,15,19]




'''

r = map(lambda x: 20 % x, range(2, 20))
print(r)
# print(tuple(r))
print(list(r)) # 在用list()方法转列表的时候，每转化一个元素时都会调用一次迭代器的__next__()方法，转化完之后，__next__对象指向的就是空了


s = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# print(tuple(s))
print(list(s))
