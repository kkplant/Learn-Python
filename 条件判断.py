#条件判断
#在Python中使用if语句实现条件判断,注意冒号和缩进规则
age=20
if age>=18:
    print("your age is ",age)
    print("adult")

age=3
if age>=18:
    print("your age is ",age)
    print('adult')
else:
    print("your age is",age)
    print("teenage")

#加入elif
age=3
if age>=18:
    print('adult')
elif age>=6:
    print('teenage')
else:
    print("kid")

#if语句的完整形式
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>

#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

#if判断条件还可以简写
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if 1:
    print('ok')

#input()函数返回的数据类型是str，用int()转换为整数
#int()函数，int()函数发现一个字符串并不是合法的数字时就会报错
s=input('birth:')
birth=int(s)
if birth>2000:
    print(s,'是00后')
else:
    print('00前')

#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：

name='小明'
result=['过轻','正常','过重','肥胖','严重肥胖']
h=1.75
w=80.5
BMI=w/(h*h)
if BMI<18.5:
    print(name,result[0])
elif BMI<25:
    print(name,result[1])
elif BMI<28:
    print(name,result[2])
elif BMI<32:
    print(name,result[3])
else:
    print(name,result[4])


	


