# -*- coding:utf-8 -*-

#计算一个字符串的MD5值
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#分块多次调用update()
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#SHA1算法
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
