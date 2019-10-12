# -*- coding:utf-8 -*-

class Test(object):
    __slots__ = ('a', 'b')

s = Test()
s.a = 'kk'
s.b = 55

print(s.a)
print(s.b)