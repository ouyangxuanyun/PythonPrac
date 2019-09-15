# Time : 2019/9/15 17:08
# Author : Fu
# Software: PyCharm
# 9-1 如何使用函数装饰器


def memo(func):
    cache = {}

    def wrap(*args, ):
        res = cache.get(args)
        # print(args)
        if not res:
            res = cache[args] = func(*args)
        return res

    return wrap

@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count

print(fibonacci(3))