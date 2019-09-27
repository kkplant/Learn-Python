# -*- coding : utf-8 -*-
# User : ChenXiong

def fib(n):
    a = 0
    b = 1
    result = []
    while a < n:
        result.append(a)
        b = a + b
        a = b
        #print(a)
    return result

#print(fib(5))
print(fib(3))