

# class Person:
#     # 实例：liming = Person('xiaoming', 'Male', '19900101', job='Student', score=100)
#     def __init__(self, name, gender='male', birth='19940213', **kwargs):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#         self.kwargs = kwargs
#
#     # 修改对象信息
#     def set_init(self, name,gender='male', birth='19940213', **kwargs):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#         self.kwargs = kwargs

# 子类


# class Student(Person):
#
#     def __init__(self,name,gender,birth,classroom,ID,**kwargs):
#         # 继承父类，并增加了班级、学号、科目、成绩
#         super(Student,self).__init__(name,gender,birth,**kwargs)
#         self.classroom = classroom
#         self.ID = ID
#         self.kwargs = kwargs
#
#         # 修改对象信息
#     def set_init_new(self, name,gender,birth,classroom,ID,**kwargs):
#         Person.set_init(name,gender,birth)
#         self.classroom = classroom
#         self.ID = ID
#         self.kwargs = kwargs

