# Time : 2019/8/4 15:24
# Author : Fu
# Software: PyCharm

from collections import deque
import pickle

q = deque([],3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

pickle.dump(q, open('../files/history', 'wb'))

q2 = pickle.load(open('../files/history', 'rb'))
print(q2)