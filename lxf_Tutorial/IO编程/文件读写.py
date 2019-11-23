# -*- coding:utf-8 -*-
'''
#打开文件
f = open('D:/Learn-Python/test.lua', 'r')
print(f.read())

#关闭文件
#使用close()方法
f.close()

#使用try语句打开关闭文件
try:
    f = open('D:/Learn-Python/test.lua', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#使用with语句打开关闭文件
with open('D:/Learn-Python/test.lua', 'r') as f:
    #一次性读取文件全部内容
    #print(f.read())
    #读取size个字节
    #print(f.read(2))
    #读取一行
    #print(f.readline())
    #读取所有内容并按行返回list
    #print(f.readlines())
    #按行读取并逐行输出（去除末尾的\n）
    for line in f.readlines():
        print(line.strip())
        
#写文件
f = open('D:/Learn-Python/test.lua', 'w')
f.write('Hello, world!\n')
f.write('Goodbye, world!')
f.close()
'''
#with语句写文件
with open('D:/Learn-Python/test.lua', 'w') as f:
    f.writelines('China')
