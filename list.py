# -*- coding:utf-8 -*-

#list是一种有序可变的集合，是Python内置的数据类型
grand=['2','1','2']
classnum=['1','2','4']
name=['a','b','c']

#穷举
#print('%s是%s年级%s班的。' %(name[0] ,grand[0],classnum[0]))
#print('%s是%s年级%s班的。' %(name[1] ,grand[1],classnum[1]))
#print('%s是%s年级%s班的。' %(name[2] ,grand[2],classnum[2]))

#循环写法
#i=0
#while i-len(name)<0:
#    print('%s是%s年级%s班的。' %(name[i] ,grand[i],classnum[i]))
#    i=i+1

list1=['a','b',1,2]
print(list1)

#正序索引首个元素
list1[0]
#逆序索引最后一个元素
list1[-1]


#往list队尾追加元素
list1.append('c')
print('追加元素:%s' %list1)

#往list中插入元素
list1.insert(2,0)
print('插入元素:%s' %list1)

#替换list元素
list1[2]=-1
print('替换元素：%s' %list1)

#删除list末尾元素
#list1.pop()
list1.pop(len(list1)-1)
print('删除队尾元素：%s' %list1)

#删除list某个元素
list1.pop(2)
print('删除某个元素：%s' %list1)

