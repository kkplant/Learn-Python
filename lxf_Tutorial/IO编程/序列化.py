# -*- coding:utf-8 -*-

import pickle
d = dict(name='Bob', age=20, score=88)
pickling1 = pickle.dumps(d)
print(pickling1)
a = dict()

with open('D:/Learn-Python/test/dump.txt', 'wb') as f:
    pickle.dump(d, f)
    print(d)

with open('D:/Learn-Python/test/dump.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)
