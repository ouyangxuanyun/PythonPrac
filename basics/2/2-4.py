# Time : 2019/8/4 11:13
# Author : Fu
# Software: PyCharm

from random import randint

d = {x: randint(60, 100) for x in 'zxvcab'}

res1 = sorted(d)

print('RES1:::', d, res1)

'''
 使用zip函数
 把字典转换成元祖，元祖可以比较大小  （69,'a'）>（60, 'b'）
'''

res2 = sorted(zip(d.values(), d.keys()))
print('RES2:::', res2)

'''
 sorted 函数key
'''

res3 = sorted(d.items(), key=lambda x: x[1])
print('RES3:::', res3)
