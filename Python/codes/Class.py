class People:
    def __init__(self, name, age, say):
        self.name = name
        self.say = say
        self.age = age

    def hello(self):
        print(str(self.age) + "岁的" + self.name + "说:", self.say)

    @staticmethod
    def tool_max(arg_list):
        return max(arg_list)


wzr = People("卓然", 18, "早安！打工人！")
wzr.hello()
# print(People.tool_max([2, 3, 4, 5, 6]))
# print(wzr.tool_max([2, 3, 42, 5, 6]))
print(wzr.__dict__)
print(wzr.__class__, wzr.__class__ == People)

print("\n------------------------------------------------\n类变量、类方法\n------------------------------------------------")


# 类方法
class Count:
    _count = 0

    def __init__(self):
        self.__class__._count += 1

    @classmethod
    def print_count(cls):
        print(cls._count)


count_obj1 = Count()
count_obj2 = Count()
count_obj3 = Count()
Count.print_count()
count_obj3.print_count()

print("\n------------------------------------------------\n静态方法\n------------------------------------------------")


# 静态方法
class ClassStatic:
    @staticmethod
    def tool_max(param_list):
        return max(param_list)


obj = ClassStatic()
print(ClassStatic.tool_max([2, 3, 4]))
print(obj.tool_max([4, 5, 6]))

print("\n------------------------------------------------\n私有变量、私有方法\n------------------------------------------------")


# 私有变量&私有方法
class ClassPrivate:
    def __init__(self, name):
        self.name = name
        self.__weight = 0
        self.__eat_weight = 0

    def eat(self):
        self.__eat_weight += 1
        print("%s又吃了一大碗饭，现在已经%d斤了，不能再吃啦！" % (self.name, self.__get_weight()))

    def set_weight(self, weight):
        self.__weight = weight
        print("天了噜！%s居然都%d斤了，真是不敢相信！" % (self.name, weight))

    def __get_weight(self):
        return self.__weight + self.__eat_weight


wzr_pri = ClassPrivate("然宝宝")
wzr_pri.set_weight(90)
wzr_pri.eat()
wzr_pri.eat()

print("\n------------------------------------------------\n继承\n------------------------------------------------")


class Human:
    count = 0

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


class Student(Human):
    def __init__(self, name, school):
        # super().__init__(name)
        super(Student, self).__init__(name)  # 需不需要传的问题
        self.school = school
        # Human.__init__(self, name)

    def get_school(self):
        print(self.school)


rbb = Student("然宝宝", "CAU")
rbb.get_name()
rbb.get_school()
print(Student.__base__)
print(isinstance(rbb, Student ), isinstance(rbb, Human))
