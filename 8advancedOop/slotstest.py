# slots用于限制实例的属性
# 但是对子类无效
class Student(object):
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass