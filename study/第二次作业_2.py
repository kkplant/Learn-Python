# -*- coding: utf-8 -*-


def Xdict(num):
    _i = 0
    a = {}
    _b = a
    for _i in range(1, num+1):
        if _i == num:
            _b[_i] = 'value'
        else:
            _b[_i] = {}
            _b = _b[_i]
    return a

print(Xdict(100))
