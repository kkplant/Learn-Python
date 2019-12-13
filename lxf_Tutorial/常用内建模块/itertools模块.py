# -*- coding:utf-8 -*-
import itertools

#count()，无限迭代器，不会自动停止
natuals1 = itertools.count(1)
print(natuals1)
for n in natuals1:
    print(n)
    if n >= 10:
        break

#count()，初始值和步进
natuals1_1 = itertools.count(start=1, step=2)
print(natuals1_1)
for n_1 in natuals1_1:
    print(n_1)
    if n_1 >= 10:
        break

#cycle()，无限重复传入的序列，不会自动停止
natuals2 = itertools.cycle('abc')
print(natuals2)
for c in natuals2:
    print(c)
    if c == 'c':
        break

#repeat()，无限重复传入的元素，第二个参数可以设置重复次数
natuals3 = itertools.repeat('AB', 2)
print(natuals3)
for r in natuals3:
    print(r)

#使用takewhile()函数中断迭代
natuals4 = itertools.count(0)
nn = itertools.takewhile(lambda x: x <= 10, natuals4)
print(list(nn))

#chain()，串联迭代对象
for ch in itertools.chain('ABC', 'xyz'):
    print(ch)

#groupby()，把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

