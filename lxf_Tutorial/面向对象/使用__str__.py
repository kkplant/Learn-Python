# -*- coding:utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    #__repr__ = __str__
    def __repr__(self):
        return 'Student object (name: %s)' % self.name

s = Student('Jack')
print(s)
print('打印实例结果为：%s' % s)
