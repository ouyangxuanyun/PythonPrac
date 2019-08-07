# Time : 2019/8/4 10:52
# Author : Fu
# Software: PyCharm
import re
from random import randint
from collections import Counter

data = [randint(0, 20) for _ in range(30)]

c = dict.fromkeys(data, 0)

for x in data:
    c[x] += 1

print(c)

'''
 使用Counter
'''

c2 = Counter(data)
print(c2)

# 统计出现频数最高的3个
res1 = c2.most_common(3)

print(res1)

'''
计算一篇文章每个单词出现个数
'''

txt = open('../files/news.txt').read()

c3 = Counter(re.split('\W+', txt))
print(c3,c3.most_common(10))
