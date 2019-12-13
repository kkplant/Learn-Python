# -*- coding:utf-8 -*-
#计算圆周率
import itertools

def pi(N):
    '计算pi的值'
    #step1：创建一个奇数序列
    #step2：取该序列的前N项
    #step3：添加正负号并用4除
    #step4：求和
    natuals = itertools.count(0)
    oddnumbers = []
    PI = 0
    for n in natuals:
        oddnumbers.append(((-1)**n)*4/(2*n + 1))
        if n == int(N) - 1:
            break
    for x in oddnumbers:
        PI = PI + x
    #return list(oddnumbers)
    return PI
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
print(pi(100000))

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')