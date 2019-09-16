# Time : 2019/9/16 22:59
# Author : Fu
# Software: PyCharm

"""
7-2 如何降低大量实例的内存开销
"""


class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level


class Player2:
    __slots__ = ['uid', 'name', 'level']

    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level


import tracemalloc

tracemalloc.start()
# start
la = [Player1(1, 2, 3) for _ in range(100000)]
lb = [Player2(1, 2, 3) for _ in range(100000)]
# end
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename') # 按照文件统计使用内存，依次注释30,31行运行对比结果
# top_stats = snapshot.statistics('lineno')  # 按照行数统计内存
for stat in top_stats[:10]: print(stat)
