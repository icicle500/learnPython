class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,score):
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
