# 装饰器
# 开闭原则， 对修改是封闭的，对扩展是开放的，用扩展解决需求变更的问题
import time


# def print_current_time(func):
#     print(time.time())
#     func()
#
# print_current_time(f1)
# print_current_time(f2)


def decorator(func):
    # *args 保证装饰不同参数的函数， **kw 保证装饰关键字参数的函数
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)  # 满足所有函数的调用方式

    return wrapper


# f = decorator(f1)
# f()


@decorator  # 上面注释的语法糖
def f1(one):
    print('This is a function 1 ' + one)


@decorator
def f2(one, two, three):
    print('This is a function 1 ' + one + two + three)


@decorator  # 关键字参数
def f3(one, two, **kw):
    print(one, two, kw)


# f3('a1','a2',a=1,b=2,c=3)

f1('1')
f2('1', '2', '3')
f3('a1', 'a2', a=1, b=2, c=3)


# def test1(*args):
#     print(args)
# test1(1,2,3)
#
# def test2(**kw):
#     print(kw)
# test2(a=1)