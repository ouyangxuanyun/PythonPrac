from Human import Human


class Student(Human):
    # sum_time = 0

    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self,name,age)  # 调用父类构造函数,注意要有self 不建议这样使用
        super(Student, self).__init__(name, age)

    #     self.name = name
    #     self.age = age
    #     self.score = 0
    #     print('init student')
    #     print('当前学生总数为:' + str(self.__class__.sum_time), self.sum_time)

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

    @classmethod
    def plus_sum(cls):
        cls.sum_time += 1
        print(cls.sum_time)

    @staticmethod
    def add(x, y):
        print(Student.sum_time)
        print('This is a static method')

    def marking(self, score):
        self.score = score

    def do_homework(self):
        super(Student, self).do_homework()
        print('child home work')


student = Student('百家小学', '小明', 100)
student.print_file()
student.do_homework()

Student.plus_sum()
Student.add(22, 33)
