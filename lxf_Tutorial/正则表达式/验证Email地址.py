# -*- coding:utf-8 -*-

import re

def is_valid_email(addr):
    re_email = re.compile(r'^(\W)+(.\w+)*@(\W)+((.\W+)+)$')
    re_email.match(addr)
    
print(is_valid_email('someone@gmail.com'))
#assert is_valid_email('someone@gmail.com')
#assert is_valid_email('bill.gates@microsoft.com')
#assert not is_valid_email('bob#example.com')
#assert not is_valid_email('mr-bob#example.com')
#print('ok')

#https://jingyan.baidu.com/article/95c9d20d007bfcec4e756113.html