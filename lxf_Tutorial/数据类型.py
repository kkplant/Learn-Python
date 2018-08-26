#整数
i=1001
print(i)

#浮点数
i=1.23e-9
print(i)

#字符串
print("I'm ok!")

i="I'm ok!"
print(i)

#使用\转义
i="I\'m \"ok\"!"
print(i)

i='I\'m \"ok\"!'
print(i)

#转义字符：\n、\t、\\
i='hello \nworld \nbaby'
print(i)

i='hello\tworld\tbaby'
print(i)

i='http:\\\www.tgbus.com'
print(i)

#r'...'或者r"..."或者r'''...'''，表示省略号中的内容默认不转义
print(r'\n \t \\')

#另一种换行方式
print('''hello
world
baby''')

#布尔值：True，False，要区分大小写，Python对大小写是敏感的
#布尔运算：大于：>,小于：<,等于：=,不等于：<>,大于等于：>=,小于等于:<=
#布尔运算：与或非：and、or、not

age=input()

if age>=18:
    print('adult')
else:
    print('teenager')

#空值 None

#变量，使用=对变量赋值
#变量名必须是大小写英文、数字和_的组合，且不能用数字开头
#Python是动态语言，定义变量的时候不需要指定数值类型

#常量，例如π。Python中通常用全部大写英文表示常量




	

