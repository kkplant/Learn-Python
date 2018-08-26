#list相关
#list列表，是Python内置的一种数据类型，是一种有序、可变的集合，可随时添加和删除其中的元素
age=[12,23,56,21,6,60]
age

#用len()函数可以计算出list列表中的元素个数
len(age)

#用索引来访问list中的，索引号从0开始计算
age[0]
age[1]

#list列表中最后一个元素，可以用正序索引（索引号）或者倒序索引，倒序索引号是-1，其他依次倒数
age[-1]
age[-2]

#在list中追加元素到末尾
age.append(70)

#在list中插入元素
age.insert(1,19)

#在list中删除末尾的元素
age.pop()

#在list中删除指定位置的元素
age.pop(0)

#在list列表中替换元素，直接赋值即可
age[1]=0

#list里面的元素数据类型可以不同
list=['abc',12,True]

#list里面得元素可以是另一个list
list=[12,[52,52],56,80]

#要取得list中的list里的元素
list[1][0]

#tuple相关
#tuple与list类似，但是tuple初始化后，元素不能再修改
#注意，当定义一个tuple的时候，元素必须确定下来
tuple=(1,2)

#定义一个空的tuple
tuple=()

#Python规定，如果定义的tuple只有一个元素要加逗号，以示和数学符号()的区别
#Python显示一个元素的tuple的时候也会加逗号
tuple=(1,)

#“可变”的tuple，定义tuple的时候，加入list，通过改变list内的元素，而tuple的元素不变
tuple=(1,[],2,3)

#练习
# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

