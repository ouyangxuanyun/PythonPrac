# Time : 2019/9/15 20:38
# Author : Fu
# Software: PyCharm
"""
9-3 带参数的装饰器
带参数的装饰器，就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂，每次根据参数返回一个特定的装饰器，然后用它去修饰其他函数
"""

import inspect


# 检查被装饰函数的参数类型
def type_assert(*ty_args, **ty_kwargs):
    def decorator(func):
        # A 获取被装饰函数的函数签名，bind（）以参数为键建立字典 参数-类型
        func_sig = inspect.signature(func)
        bind_type = func_sig.bind_partial(*ty_args, **ty_kwargs).arguments

        def wrap(*args, **kwargs):
            # B ...
            for name, obj in func_sig.bind(*args, **kwargs).arguments.items():
                type_ = bind_type.get(name)
                if type_:
                    if not isinstance(obj, type_):
                        raise TypeError('%s must be %s' % (name, type_))
            return func(*args, **kwargs)

        return wrap

    return decorator


@type_assert(int, list, str)
def f1(a, b, c):
    pass


@type_assert(c=str)
def f2(a, b, c):
    pass


f1(4, [], 'aaa')  # 正常
f1(4, [], 123)  # TypeError: c must be <class 'str'>
f2('aaa', 123, [])  # TypeError: c must be <class 'str'>
