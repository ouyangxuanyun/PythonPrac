from itertools import islice

f = open('/var/log/dpkg.log.1')

for line in islice(f, 100 - 1, 300):
    print(line)

'''
自己实现简单的islice
'''


def my_islice(iterable, start, end, step=1):
    tmp = 0
    for i, x in enumerate(iterable):
        if i >= end:
            break

        if i >= start:
            if tmp == 0:
                tmp = step
                yield x
            tmp -= 1


print(list(my_islice(range(100, 150), 10, 20, 3)))
print(list(islice(range(100, 150), 10, 20, 3)))


'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

'''