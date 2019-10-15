# -*- coding:utf-8

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60 and self.score <80:
            return 'B'
        elif self.score >= 80 and self.score <=100:
            return 'A'
        elif self.score >= 0 and self.score <60:
            return 'C'
        else:
            raise ValueError('This is wrong number.')
        
a = Student('a', 65)
b = Student('b', 95)
c = Student('c', 55)
d = Student('d', -5)
e = Student('e', 200)
#print('a is %s \nb is %s \nc is %s \nd is %s \ne is %s \n' % (a.get_grade(), b.get_grade(), c.get_grade(), d.get_grade, e.get_grade))