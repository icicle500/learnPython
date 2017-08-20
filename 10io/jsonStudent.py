import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s =Student('Bob',20,88)
s_dumps=json.dumps(s,default=lambda obj:obj.__dict__)
print(s_dumps)
print(json.loads(s_dumps, object_hook=dict2student))