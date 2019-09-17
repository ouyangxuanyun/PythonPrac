# Time : 2019/9/15 20:01
# Author : Fu
# Software: PyCharm

'''
9-2 被装饰的函数保存元数据
f.__name__: 函数名字
f.__doc__:函数文档字符串
f.__module__: 函数所属模块名
f.__dict__: 属性字典
f.__defaults: 默认参数元组
'''

from functools import update_wrapper, wraps


def f(a: int, b: str) -> int:
    """
    function f: always return a number
    :return: int
    :param a: 
    :param b: 
    :return: 
    """

    return 100


print(f.__dict__,
      f.__name__,
      f.__doc__,
      f.__module__,
      f.__annotations__)


def my_decorator(func):
    # 方法1：直接用wraps装饰原函数。注意@wraps有参数，否则报错AttributeError: 'functools.partial' object has no attribute
    @wraps(func)
    def wrap(*args, **kwargs):
        """
        某功能包裹函数
        :param args:
        :param kwargs:
        :return:
        """
        return func(*args, **kwargs)
    # 方法2：使用update_wrappper()
    # update_wrapper(wrap, func)
    return wrap


@my_decorator
def xxx_func(a, b):
    """
    xxx_func 函数文档：
    :param a:
    :param b:
    :return:
    """
    return 100


print(xxx_func.__name__)
print(xxx_func.__doc__)
