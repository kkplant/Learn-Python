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
    return s                 #return语句必然是要写在第一个缩进块内，因为执行到return函数就结束了

#默认参数
def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

#设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def info(name,city,age=6):
    print(name)
    print(age)
    print(city)

#定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=[]):
    L.append('end')
    return L
#本例如果多次使用默认参数调用函数，会出现错误结果
#用None作为默认参数解决本例问题
def add_end(L=None):
    if L is None:
        L=[]
        L.append('end')
    else:
        L.append('end')
    return L

#可变参数
#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
#计算平方和a^2+b^2+c^...n^2
def sum_squr(nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
#*nums表示把nums这个list的所有元素作为可变参数传进去
#下例写法，可以直接把元素逐个写到括号中传入函数
def sum_squr(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
#参数传入1
sum_squr(1,2,3)
#参数传入2
i=[1,2,3]
sum_squr(*i)

#关键字参数
#关键字参数允许你传入0个或任意个含"参数名的参数"，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

def person1(name,age,**kw):
    dict={'name':name,'age':age,'other':kw}
    return dict

def person2(name,age,**kw):
    return name,age,kw

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
d={'city':'fz','kk':78}
person2('cx',5,**d)
#**d表示把d这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是d的一份拷贝，对kw的改动不会影响到函数外的d

#命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
    return name,age,city,job

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person1(name,age,*agr,city,job):
    return name,age,agr,city,job

#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person('cx',6,'fz','zy')
#这种调用会报错
#由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数

#命名关键字参数可以有缺省值，从而简化调用
def person2(name,age,*,city='fz',job):
    return name,age,city,job

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
#请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#必选参数：x
#默认参数：x=56
#可变参数：*x
#命名关键字参数：*,x
#关键字参数：**x
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*args,d,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'d=',d,'kw=',kw)
#通过一个tuple和dict，也可以调用上述函数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
l=(1,2,3,4,'aa')
d={'name':'cx','city':'fz'}
f2(*l,d=90,**d)                  #命名关键字参数必须传入带参数名的参数，应该不能用tuple和dict传参数


#小结
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。



