# -*- coding:utf-8 -*-
'''
with语句与上下文管理器
https://www.cnblogs.com/nnnkkk/p/4309275.html
'''

#使用try...finally管理文件
try:
    f1 = open('D:/Learn-Python/1.py', 'r')
    f1.read()
finally:
    if f1:
        f1.close()
print(f1)

#使用with语句，简化代码
with open('D:/Learn-Python/1.py', 'r') as f2:
    f2.read()
print(f2)


'''
with语句中的函数是上下文管理器，并非只有open()函数才能使用with。
只要正确实现了上下文管理，就可以使用with语句。
'''
#实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):  #自定义类
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()
print(q)

#使用contextlib标准库的contextmanager模块简化上下文管理
from contextlib import contextmanager

class Query1(object):
    def __init__(self, name):
        self.name = name
    def query1(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q1 = Query1(name)
    yield q1
    print('End')

with create_query('James') as q1:
    q1.query1()
print(q1)

#使用closing把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

        