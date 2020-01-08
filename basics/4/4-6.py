# Time : 2020/1/9 0:21
# Author : Fu
# Software: PyCharm

from random import randint
from itertools import chain
from functools import reduce

chinese = [randint(60, 100) for _ in range(20)]
math = [randint(60, 100) for _ in range(20)]
english = [randint(60, 100) for _ in range(20)]

t = []
for s1, s2, s3 in zip(chinese, math, english):
    t.append(s1 + s2 + s3)

t2 = list(map(sum, zip(chinese, math, english)))
t3 = [sum(s) for s in zip(chinese, math, english)]

for x in chain([1, 2, 3], [4, 5, 6, 7], [8, 9]):
    print(x)

s = 'abc:123|xyz:678|asdf\tjzka'

print(list(map(lambda ss: ss.split('|'), s.split(':'))))
print(list(chain(*map(lambda ss: ss.split('|'), s.split(':')))))

result = list(reduce(lambda it_s, sep: chain(*map(lambda ss: ss.split(sep), it_s)), ':|\t', [s]))
print(result)
