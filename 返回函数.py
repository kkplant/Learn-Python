# -*- coding: utf-8 -*-
#User:chenxiong

def createCounter():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter

#闭包实现
#def createCounter1():
#    def counter(i):
#        i = 0
#        def num():
#            #i = 0
#            return i+1
#        return num
#        count = [0]
#        count[0] = counter(i)
#    return count    

def  createCounter1():
    s = [0]
    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter1()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

