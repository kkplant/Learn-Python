# -*- coding:utf-8 -*-
#Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

import hmac, hashlib
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5') #传入的key和message需要是bytes类型
print(h.hexdigest())
m = hashlib.md5()
m.update(str(message).encode('utf-8'))
print(m.hexdigest())
