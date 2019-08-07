# Time : 2019/8/4 11:25
# Author : Fu
# Software: PyCharm
from functools import reduce
from random import randint, sample

data = sample('abcdefg', randint(3, 6))

'''
快速找到多个字典中的公共键,利用集合
'''

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print(s1, s2, s3)

print(s1.keys() & s2.keys() & s3.keys())

'''
使用reduce
'''
res = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))
