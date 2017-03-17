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

#使用递归函数需要注意防止栈溢出
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
#解决递归调用栈溢出的方法是通过尾递归优化
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

def fact1(n,m=1):
    if n==1:
        return m
    return fact1(n-1,n*m)
#加个参数x,看看函数迭代了几次
def fact2(n,x=0,m=1):
    if n==1:
        return m,x
    return fact2(n-1,x+1,n*m)


#小结
#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

#练习
#汉诺塔的移动可以用递归函数非常简单地实现。
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

def move(n,a='A',b='B',c='C'):
    if n==1:
        print('move',a,'-->',c)
        return
    else:
        move(n-1,a,c,b)                #b,c柱子直接倒腾
        




def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)