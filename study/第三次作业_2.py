# -*- coding: utf-8 -*-

#import os
#import sys
i = 0
i += 1
fileName = '第三次_2_{}.py'.format(i).encode('utf-8')
print('第{}个副本的文件名为：'.format(i) + str(fileName))
codeDoc_1 = open(__file__, 'r' , encoding='utf-8')
codeDoc_2 = open(fileName, 'w')

codes = None
for codes in codeDoc_1.readlines():
    print(codes)
    codeDoc_2.writelines(codes)#(codes.encode('utf-8'))
    