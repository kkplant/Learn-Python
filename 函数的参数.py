#函数的参数
#Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数
#位置参数
import math

def power(x):
    return x*x

def power(x,n):
    s=1
    while n>0:
        s=s*x
        n=n-1
        return s

