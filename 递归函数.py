# -*- coding: utf-8 -*-

#递归函数
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(x):
    if x<0:
        print('不能是负数')
        return
    if x==0:
        return 1
    else:
        sum=1
        while x>0:
            sum=sum*x
            x=x-1
        return sum

def fact1(x):
    if x<=1:
        return 1
    else:
        return fact1(x-1)*x

def jc(x):
    sum=1
    while x>0:
        sum=sum*x
        x=x-1
    return sum

def jc1(x):
    if x<0:
        print('不能是负数')
    else:
        sum=1
        while x>0:
            sum=sum*x
            x=x-1
        return sum

#递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。


