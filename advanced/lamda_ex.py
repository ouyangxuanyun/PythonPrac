def add(x, y):
    return x + y


print(add(1, 2))

f = lambda x, y: x + y

print(f(1, 2))


# python的三元表达式
t = 1
f = 2
r = t if t >f else f
print(r)
