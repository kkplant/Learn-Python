# -*- coding: utf-8 -*-

import math

class Happy(object):
    _id = -1
    _num = 0
    num_output = 0

    def __init__(self, num):
        Happy._id += 1
        self._id = Happy._id
        self._num = int(num)

    def Return(self):
        num_output = (pow(-1, self._id))*self._num
        return num_output


if __name__ == '__main__':
    a = Happy(1)
    print(a._id)
    b = Happy(2)
    print(b._id)
    print (a.Return() + b.Return())
