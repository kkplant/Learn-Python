# -*- coding:utf-8 -*-
#if语句从上往下判断，判断到True，就执行该判断的语句，并忽略剩余的语句
age=20
if age>=18:
    print('成年')
elif age>=6:
    print('青少年')
else:
    print('儿童')

age=20
if age>=6 :#and age<18:
    print('青少年')
elif age>=18:
    print('成年')
else:
    print('儿童')

#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖

height=1.75
weight=80.5
bmi=weight/(height*height)

