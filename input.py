# -*- coding:utf-8 -*-
loop=1
names=[]
while loop==1:
    name=input('请输入姓名：')
    names.append(name)
    loop1=1
    print('录入成功！')
    while loop1==1:
        #print('继续录入，请输入\"Y\"')
        #print('放弃录入，请输入\"N\"')
        a=input('是否继续录入？(Y/N)')
        if a is 'Y':
            loop1=0
            loop=1
        elif a is 'N':
             loop1=0
             loop=0
             #break
        else:
            print('输入错误！')
            print('继续录入，请输入\"Y\"')
            print('放弃录入，请输入\"N\"')
            loop1=1
            loop=0
print(names)
