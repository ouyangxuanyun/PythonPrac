from functools import reduce

list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_y = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

r = reduce(lambda x, y: x + y, list_x)
print(r)
