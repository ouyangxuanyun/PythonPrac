# 列表推导式
# [],{},(), list, set, dict, tuple
a = [1,2,3,4,5,6]

b = [i**3 for i in a if i < 100]
print(b)


students = {
    '小a': 14,
    '小b':17
}

r = {value:key + '00' for key, value in students.items()}
print(r)