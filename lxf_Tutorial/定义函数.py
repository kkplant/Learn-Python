#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

#函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None

#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

#pass也可以用在其他语句中
if i>1:
    pass

#参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError;如果参数类型不对，Python解释器就无法帮我们检查
#数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

#返回多个值
#Python的函数返回多值其实就是返回一个tuple
import math                             #导入math包，并允许后续代码引用math包里的函数

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

#练习
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0 的两个解。
import math

def quadratic(a,b,c):
    if a==0:
        x=-c/b
        return x
    else:
        k=b*b-4*a*c
        if k>=0:
            x1=(-b+math.sqrt(k))/(2*a)
            x2=(-b-math.sqrt(k))/(2*a)
            return x1,x2
        else:
            return '无解'



