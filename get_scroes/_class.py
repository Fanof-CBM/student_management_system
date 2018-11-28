# 以下为底层类
import sys


class Data:

    def __init__(self,day=00,month=00,year=2018):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls,data_str=input('ex:dd-mm-yyyy')):
        flag = str(data_str)
        day, month, year = map(int, flag.split('-'))
        data1 = cls(day, month, year)
        return data1


    def new_self(self):
        self.day,self.month,self.year = [x for x in v.from_string().__dict__.values()]
        print(self.day,'-',self.month,'-',self.year,sep='')

try:
    v = Data().from_string()
    v.new_self()
except:
    print(ValueError)


# 父类


class Person:
    # 实例：liming = Person('xiaoming', 'Male', '19900101', job='Student', score=100)
    def __init__(self, name, gender='male', birth='19940213', **kwargs):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.kwargs = kwargs

    # 修改对象信息
    def set_init(self, name,gender='male', birth='19940213', **kwargs):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.kwargs = kwargs

# 子类


class Student(Person):

    def __init__(self,name,gender,birth,classroom,ID,**kwargs):
        # 继承父类，并增加了班级、学号、科目、成绩
        super(Student,self).__init__(name,gender,birth,**kwargs)
        self.classroom = classroom
        self.ID = ID
        self.kwargs = kwargs

        # 修改对象信息
    def set_init_new(self, name,gender,birth,classroom,ID,**kwargs):
        Person.set_init(name,gender,birth)
        self.classroom = classroom
        self.ID = ID
        self.kwargs = kwargs

