# -*- coding:utf-8 -*-

import os

#操作文件和目录
#查看当前目录的绝对路径
print(os.path.abspath('.'))

#创建新目录
#首先把新目录的完整路径表示出来
os.path.join('D:/Learn-Python/', 'filetest')
#然后创建目录
os.mkdir('D:/Learn-Python/filetest')
#删除目录
os.rmdir('D:/Learn-Python/filetest')

#拆分路径
print(os.path.split('D:/Learn-Python/test'))
print(os.path.split('D:/LePython/test'))              #不存在的路径
print(os.path.split('D:/Learn-Python/test.lua'))
print(os.path.split('D:/Learn-Python/test.docx'))     #不存在的文件

#获取文件扩展名
print(os.path.splitext('D:/Learn-Python/test/test.lua'))

#列出当前目录下的所有目录
name = [x for x in os.listdir('.') if os.path.isdir(x)]
print(name)

#列出当前目录下的所有.py文件
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] 
print(files)
