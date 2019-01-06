# map 类

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1000,1000,1000,1000,1000,1000,1000,1000]

def squre(x):
    return x * x


for x in list_x:
    squre(x)


r = map(squre, list_x)
print(list(r))


t = map(lambda x,y: x*x + y, list_x,list_y)
print(list(t))