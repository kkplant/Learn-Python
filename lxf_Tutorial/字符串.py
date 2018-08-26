#Python3中，字符串以Unicode编码
#Python字符串支持多语言

i='中国chinaにほんご'
print(i)

#函数ord()用于提取字符串（单个字符）的整数表示
ord('中国')

#函数chr()把编码转换为对应的字符
chr(66)

#若知道编码的十六进制，可以用\u写字符串
'\u6587'

#Python对bytes类型的数据用带b前缀的单引号或双引号表示
i=b'abc'

#以Unicode表示的str通过encode()方法可以编码为指定的字节数据bytes
'abc'.encode('ascii')
'中国'.encode('utf-8')
'中国'.encode('gb2312')

#在bytes中，无法显示为ASCII字符的字节，用\x##显示

#通过decode()把字节数据bytes变为字符串str
b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8')

#用len()函数计算字符串有多少个字符或者计算字节数据bytes有多少字节
len('中国')
len(b'abc')

#!/usr/bin/env python3   
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码

#用%运算符格式化字符串
#%s表示用字符串替换，%d、%f、%s、%x分别表示用整数、浮点数、字符串、十六进制整数替换
#代码中有几个%?占位符，后面就要跟几个变量或者值，并一一顺序对应，多个时加括号
x=72
y=85
i=(y-x)/x*100
print('%.1f%%'%i)






