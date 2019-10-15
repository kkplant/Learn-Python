# -*- coding:utf-8 -*-

#print()打印问题变量
def foo(s):
    n = int(s)
    print('>>>n = %d' % n)
    return 10 / n

def main():
    foo('0')

#main()

#断言
def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main1():
    foo1('0')

#main1()

#logging
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

