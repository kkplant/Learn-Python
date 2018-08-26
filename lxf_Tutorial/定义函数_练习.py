# -*- coding:utf-8 -*-
#定义一个函数，用于求解一元二次方程
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type:a not int() or float()')
    else:
        pass
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand type:b not int() or float()')
    else:
        pass
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand type:c not int() or float()')
    else:
        pass
    if a==0:
        if b==0:
            print('等式不成立！')
            return
        else:
            x=-c/b
            return float(x)
    elif a>0 or a<0:
        delta=b*b-4*a*c
        if delta==0:
            x1=-b/2*a
            x2=-b/2*a
            return float(x1),float(x2)
        elif delta>0:
            x1=(-b+math.sqrt(delta))/2*a
            x2=(-b-math.sqrt(delta))/2*a
            return float(x1),float(x2)
        elif delta<0:
            return
        else:
            return
    else:
        pass

print('分别输入一元二次方程的参数a、b、c')
a=int(input('参数a:'))
b=int(input('参数b:'))
c=int(input('参数c:'))
s=quadratic(a,b,c)
if s is None:
    print('该一元二次方程无实数根')#:\n x1=%d,x2=%d' %(s[0],s[1]))
elif s[0]==s[1]:
    print('该一元二次方程有两个相等的实数根:\n x1=x2=%s' %s[0])
elif s[0]>s[1] or s[0]<s[1]:
    print('该一元二次方程有两个不相等的实数根:\n x1=%s,x2=%s' %(s[0],s[1]))
else:
    pass


