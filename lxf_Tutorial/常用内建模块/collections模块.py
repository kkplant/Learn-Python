# -*- coding:utf-8 -*-

#collections模块提供有用的集合类
from collections import namedtuple,deque,defaultdict,OrderedDict,ChainMap,Counter

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)

#deque,可实现高效插入和删除的双向列表
q = deque(['a', 'b', 'c'])
q.append('x')
q.append('y')
print(q)
q.appendleft(1)
q.appendleft(2)
print(q)

q.pop()
print(q)
q.popleft()
print(q)

#defaultdict,字典的key不存在的时候传回默认值
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#OrderedDict,创建字典按照插入顺序排队
od1 = OrderedDict([('a', 1),('b', 2),('c', 3)])
print(od1)
od2 = OrderedDict()
od2['z'] = 3
od2['x'] = 1
od2['y'] = 2
print(od2)
print(list(od2.keys()))

#使用OrderedDict创建FIFO（先进先出）的字典
from collections import OrderedDict

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

od3 = LastUpdateOrderedDict(2)
od3['a'] = 1
od3['b'] = 2
print('od3:', od3)

#ChainMap可以把一组dict串起来组成逻辑上的dict

#Counter计数器,dict的一个子类
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)