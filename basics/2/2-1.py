# Time : 2019/8/4 10:20
# Author : Fu
# Software: PyCharm
from random import randint

'''
 过滤列表
'''
data = [randint(-10, 10) for _ in range(10)]

res1 = list(filter(lambda x: x >= 0, data))

res2 = [x for x in data if x > 0]

print(res1, res2)

'''
 过滤字典
'''

data2 = {x: randint(60, 100) for x in range(1, 21)}

res3 = {k: v for k,v in data2.items() if v > 90 }

print(res3)


'''
过滤集合
'''

s = set(data)

res4 = {x for x in s if x %3 ==0}

print(res4)

pass
