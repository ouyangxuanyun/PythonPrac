# Time : 2019/9/22 11:09
# Author : Fu
# Software: PyCharm

"""
 7-7 环状数据结构中管理内存
"""

import weakref


class Node:
    def __init__(self, data):
        print(data)
        self.data = data
        self._left = None
        self.right = None

    def add_right(self, node):
        self.right = node
        node._left = weakref.ref(self)

    @property
    def left(self):
        return self._left()

    def __str__(self):
        return 'Node: <%s>' % self.data

    def __del__(self):
        print('in __del__: delete %s' % self)


def create_linklist(n):
    head = current = Node(1)
    for i in range(2, n+1):
        node = Node(i)
        current.add_right(node)
        current = node
    return head

head = create_linklist(100)
head = None


import time
for _ in range(100):
    time.sleep(1)
    print('run ...')
input('wait ...')