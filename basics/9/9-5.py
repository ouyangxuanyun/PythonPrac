# Time : 2019/9/15 22:06
# Author : Fu
# Software: PyCharm

"""
9-5 在类中定义装饰器
实现 一个能将函数调用信息记录到日志的装饰器
1： 把每次函数调用时间，执行时间，调用次数写入日志
2：可以对被修饰函数分组，调用信息记录到不同日志
3：动态修改参数，比如日志格式
4：动态打开关闭日志输出功能
"""

import time
import logging

DEFAULT_FORMAT = '%(func_name)s -> %(call_time)s\t%(used_time)s\t%(call_n)s'


class CallInfo:
    def __init__(self, log_path, format_=DEFAULT_FORMAT, on_off=True):
        self.log = logging.getLogger(log_path)
        self.log.addHandler(logging.FileHandler(log_path))
        self.log.setLevel(logging.INFO)
        self.format = format_
        self.is_on = on_off

    # 装饰器方法
    def info(self, func):
        _call_n = 0

        def wrap(*args, **kwargs):
            func_name = func.__name__
            call_time = time.strftime('%x %X', time.localtime())  # 年月日分秒时格式
            t0 = time.time()
            res = func(*args, **kwargs)
            used_time = time.time() - t0
            nonlocal _call_n
            _call_n += 1
            call_n = _call_n
            if self.is_on:
                info_dict = {'call_time': call_time}
                self.log.info(self.format % locals())
            return res

        return wrap

    def set_format(self, format_):
        self.format = format_

    def turn_on_off(self, on_off):
        self.is_on = on_off


# locals 函数作用：函数中的局部变量：变量值 的字典
def f():
    x = 1
    y = [1, 2, 3]
    z = 'abc'
    print(locals())


# f()  # {'x': 1, 'y': [1, 2, 3], 'z': 'abc'}


"""
测试代码
"""
import random

ci1 = CallInfo('mulog1.log')
ci2 = CallInfo('mulog2.log')


@ci1.info
def f():
    sleep_time = random.randint(0, 6) * 0.1
    time.sleep(sleep_time)


@ci1.info
def g():
    sleep_time = random.randint(0, 8) * 0.1
    time.sleep(sleep_time)


@ci2.info
def h():
    sleep_time = random.randint(0, 7) * 0.1
    time.sleep(sleep_time)


# ci1.set_format('%(func_name)s -> %(call_n)s')
for _ in range(30):
    random.choice([f, g, h])()
