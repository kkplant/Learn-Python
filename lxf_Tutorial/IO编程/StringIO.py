# -*- coding:utf-8 -*-

#创建StringIO
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
#读取StringIO
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
