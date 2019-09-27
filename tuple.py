# -*- coding:utf-8 -*-

#tuple,元组是一种有序不可变的集合，是Python内置的数据类型
name=('a','b','c',1)
print(name)

#空tuple
a=()
print(a)

#单元素tuple
b1=(1)                #这种写法不是定义tuple，而是一个数字
print(b1)

b2=(1,)               #加个逗号，消除歧义
print(b2)

#tuple嵌套
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[1][2])

#tuple嵌套list,产生一个“可变”tuple
tuple4=(1,'a',2,'b')
list1=['A','B']
tuple5=(tuple4,list1,3)
print(tuple5)
print('%s%s%s' %(tuple5[0][0],tuple5[1][0],tuple5[2]))

tuple5[1][0]='a'
print(tuple5)
print('%s%s%s' %(tuple5[0][0],tuple5[1][0],tuple5[2]))
