from collections import namedtuple

'''
 Q: 如何为元祖中的每个元素命名，提高程序可读性
 1  定义常量
'''
NAME = 0
AGE = 1
SEX = 2
EMAIL = 3

student = ('Jin', 16, 'male', 'jim2018@qq.com')

print(student[NAME], student[EMAIL])

'''
 2 使用namedtuple
'''

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jin', 16, 'male', 'jim2018@qq.com')
s2 = Student(name='Jin', age=16, sex='male', email='jim2018@qq.com')

print(s.name, isinstance(s,tuple))
