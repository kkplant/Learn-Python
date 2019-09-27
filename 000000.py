# -*- coding : utf-8 -*-
# User : ChenXiong

#squared = [x**2 for x in range(8) if not x%2]
#print(squared)

i = 0
while i < 11:
    print(i)
    i = i + 1

j = range(0,11)
for k in j:
    if k < 11:
        print(k)
    
m = input('输入数字')
n = int(m)
if n < 0:
    print('%s是负数'%m)
elif n > 0:
    print('%s是正数'%m)
else:
    print('%s等于0'%m)

