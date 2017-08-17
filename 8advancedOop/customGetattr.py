class Student(object):
    def __init__(self):
        self.name = 'ice'

    def __getattr__(self, attr):
        raise AttributeError('没这属性，不要乱调用')


# 如果类中没有要调用的属性，便会从__getattr__尝试获取属性
