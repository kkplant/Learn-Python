# -*- coding:utf-8 -*-

#struct模块用于处理字节数据类型
import struct
#pack函数可把任意数据类型变为bytes（字节）
date1 = struct.pack('>I', 1024)  #>表示大端字节序，I表示4字节无符号整数
print(date1)

#unpack把bytes变成相应的数据类型
date2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')  #H表示2字节无符号整数
print(date2)

#分析位图文件
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
date3 = struct.unpack('<ccIIIIIIHH', s)
print(date3)
if date3[0] + date3[1] == b'BM':
    print('%s表示Windows位图' %(date3[0] + date3[1]))
elif date3[0] + date3[1] == b'BA':
    print('%s表示OS/2位图' %(date3[0] + date3[1]))
else:
    print('%s表示未知格式' %(date3[0] + date3[1]))
print('位图大小：%s' %date3[2])
print('保留位：%s' %date3[3])
print('实际图像偏移量：%s' %date3[4])
print('Header的字节数：%s' %date3[5])
print('图像宽度：%s' %date3[6])
print('图像高度：%s' %date3[7])
print('颜色数：%s' %date3[9])
