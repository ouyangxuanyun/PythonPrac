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

'''
用于序列化的两个模块
　　json：用于字符串和Python数据类型间进行转换
　　pickle: 用于python特有的类型和python的数据类型间进行转换
　　json提供四个功能：dumps,dump,loads,load
　　pickle提供四个功能：dumps,dump,loads,load

pickle可以存储什么类型的数据呢？
1 所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
2 由任何原生类型组成的列表，元组，字典和集合。
3 函数，类，类的实例



使用pickle模块有几个要点：

1 首先一定要先import pickle，这个笔者上一讲也强调过

2 打开文件的格式一定要是b模式，读要用rb模式，写要用wb模式

3 写要用dunp函数，读要用load函数
'''