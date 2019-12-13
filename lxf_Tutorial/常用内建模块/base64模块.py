# -*- coding:utf-8 -*-

import base64
str1 = base64.b64encode(b'binary\x00string')
print(str1)
str2 = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(str2)

#urlsafe,把+、/分别变成-、_
str3 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(str3)
str4 = base64.urlsafe_b64decode('abcd--__')
print(str4)
