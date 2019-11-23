# -*- coding:utf-8 -*-

import re
#匹配
#匹配成功，返回match对象
ree1 = re.match(r'00\d','007')
print(ree1)

#匹配失败，返回None
ree2 = re.match(r'00\d','00A')
print(ree2)

#匹配一个数字：\d
if re.match(r'\d','9'):
    print('\\d match \'9\'')
else:
    print('\\d not match \'9\'')

if re.match(r'\d','abc'):
    print('\\d match \'abc\'')
else:
    print('\\d not match \'abc\'')

if re.match(r'\d','a07'):
    print('\\d match \'a07\'')
else:
    print('\\d not match \'a07\'')

#匹配一个字母或数字：\w
if re.match(r'\w','9'):
    print('\\w match \'9\'')
else:
    print('\\w not match \'9\'')

if re.match(r'\w','a'):
    print('\\w match \'a\'')
else:
    print('\\w not match \'a\'')    

#匹配任意字符：\.
if re.match(r'\.','9'):
    print('\\. match \'9\'')
else:
    print('\\. not match \'9\'')

if re.match(r'\.','a'):
    print('\\. match \'a\'')
else:
    print('\\. not match \'a\'')

if re.match(r'\.','+'):
    print('\\. match \'+\'')
else:
    print('\\. not match \'+\'')



#切分字符串
ree3 = re.split(r'\s','a b  c')
print(ree3)
ree4 = re.split(r'\s+','a b  c')
print(ree4)
ree5 = re.split(r'[\s\,]+','a, b  c')
print(ree5)
ree6 = re.split(r'[\s\,\;]+','a, b ; c')
print(ree6)

#分组

