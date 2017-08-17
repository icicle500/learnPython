class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  #美化给用户显示的实例
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__  #美化给开发者显示的实例