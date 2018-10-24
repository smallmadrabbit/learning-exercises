class Student(object):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    def print_info(self):
        print('Student name is %s , age is %d' % (self.name, self.age))


class Teacher(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return 'Teacher name is %s, age is %d' % (self.__name, self.__age)


class Master(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            print('score value not allow less than zero')
        else:
            self.__score = value


if __name__ == '__main__':
    bart = Student('zhangsan', 11)
    tea = Teacher('lisi', 12)
    master = Master()
    master.name = 11
    master.age = 20
