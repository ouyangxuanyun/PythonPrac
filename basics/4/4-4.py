# Time : 2019/8/4 22:31
# Author : Fu
# Software: PyCharm

from decimal import Decimal


class FloatRange:
    def __init__(self, a, b, step):
        self.a = Decimal(str(a)) # 要先把float转换成字符串，不然Decimal接收到是是float类型丢失精度
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step


fr = FloatRange(3.0, 4.0, 0.2)
for x in fr:
    print(x)
print('-' * 20)
for x in reversed(fr):
    print(x)


'''
decimal模块用于十进制数学计算，它具有以下特点：
1.提供十进制数据类型，并且存储为十进制数序列；
2.有界精度：用于存储数字的位数是固定的，可以通过decimal.getcontext（）.prec=x 来设定，不同的数字可以有不同的精度
3.浮点：十进制小数点的位置不固定（但位数是固定的）

decimal的构建：
可以通过整数、字符串或者元组构建decimal.Decimal，对于浮点数需要先将其转换为字符串

 
decimal的context：
decimal在一个独立的context下工作，可以通过getcontext来获取当前环境。例如前面提到的可以通过decimal.getcontext().prec来设定小数点精度（默认为28）

'''

'''
只要迭代器实现了 __reverserd__ 方法则此迭代器可直接使用reversed进行反向迭代 
'''