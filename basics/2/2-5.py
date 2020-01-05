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


'''
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法
map() 函数语法：

map(function, iterable, ...)
参数
function -- 函数 
iterable -- 一个或多个序列 


'''


'''
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

语法
reduce() 函数语法：

reduce(function, iterable[, initializer])
参数
function -- 函数，有两个参数 
iterable -- 可迭代对象 
initializer -- 可选，初始参数 
'''