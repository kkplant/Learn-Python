#-*- coding:utf-8 -*-
import math
def pp(*args):
    #if num==():
    if args==():
        return 0
    else:
        sum=1
        for x in args:
            sum=sum*x
        return sum

print(pp())
print(pp(0,))
print(pp(1,))
print(pp(1,2))
print(pp(5,6,7))

print('pp(5) =', pp(5))
print('pp(5, 6) =', pp(5, 6))
print('pp(5, 6, 7) =', pp(5, 6, 7))
print('pp(5, 6, 7, 9) =', pp(5, 6, 7, 9))
if pp(5) != 5:
    print('测试失败!')
elif pp(5, 6) != 30:
    print('测试失败!')
elif pp(5, 6, 7) != 210:
    print('测试失败!')
elif pp(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        pp()
        print(pp())
        print('测试失败!')
    except TypeError:
        print('测试成功!')
