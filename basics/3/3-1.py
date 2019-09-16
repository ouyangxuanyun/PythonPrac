# Time : 2019/8/4 16:11
# Author : Fu
# Software: PyCharm
from functools import reduce

s = 'ab;cd|efg|hi,jkl|mm\topg;rst,uvw\txyz'

t = []
res1 = list(map(t.extend, [ss.split('|') for ss in s.split(';')]))
print(t)


def my_split(s, seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss: t.extend(ss.split(sep)), res))
        res = t
    return res


res2 = my_split(s, ',;|\t')
print(res2)


def my_split2(s, seps):
    return reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), seps, [s])

res3 = my_split2(s, ',;|\t')
print(res3)

'''
使用正则表达式
'''

import re

res4 = re.split('[,;|\t]+',s)
print(res4)
