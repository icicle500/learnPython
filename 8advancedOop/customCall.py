class Student(object):
    def __init__(self,name,test):
        self.name=name
        self.test=test
    def __call__(self):
        print('my name is %s' % self.name)
    
# __call__直接对实例进行调用
