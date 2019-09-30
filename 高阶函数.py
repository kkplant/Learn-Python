# -*- coding:utf-8 -*-
from functools import reduce

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    name = name[0].upper()+name[1:len(name)].lower()
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)


#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    from functools import reduce
    if L == []:
        print('输入不能为空')
    else:
        def mul(x,y):
            return x*y
    return reduce(mul,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    from functools import reduce
    #for i in range(len(s)):
    #    if s[i] == '.':
    #        num1 = list(map(int,s[0:i]))
    #        num2 = list(map(int,s[i+1:]))
    num1 = list(map(int,s[0:s.index('.')]))
    num2 = list(map(int,s[s.index('.')+1:]))
    def fn1(x,y):
        return x*10+y
    #def fn2(a,b):
    #   return a*10+b
    return reduce(fn1,num1)+reduce(fn1,num2)/10**len(num2)


#请利用filter()筛选出回文数
def is_palindrome(s):
    num = str(s)
    for i in len(num):
        if num[i] == num[len(num)-1-1*i]:
            return True
        else:
            return False

print(filter(is_palindrome,[123,12321]))


#fasffds