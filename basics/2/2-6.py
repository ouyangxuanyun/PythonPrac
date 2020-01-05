# Time : 2019/8/4 15:17
# Author : Fu
# Software: PyCharm

from collections import OrderedDict
from time import time

d = OrderedDict()
d['Jim'] = (1, 34)
d['Leo'] = (2, 37)
d['Bob'] = (3, 39)

for k in d:
    print(k)


'''

遍历一个普通字典(dict)，返回的数据和定义字典时的字段顺序是不一致的
有序字典(orderedDict)可以按字典中元素的插入顺序来输出

注意：
    有序字典的作用只是记住元素插入顺序并按顺序输出。
    如果有序字典中的元素一开始就定义好了，后面没有插入元素这一动作，
    那么遍历有序字典，其输出结果仍然是无序的，因为缺少了有序插入这一条件，
    所以此时有序字典就失去了作用，所以有序字典一般用于动态添加并需要按添加顺序输出的时候。

如下面这个列子：
import collections

my_order_dict = collections.OrderedDict(name="lowman", age=45, money=998, hourse=None)

for key, value in my_order_dict.items():
    print(key, value)
'''