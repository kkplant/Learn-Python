# -*- coding: utf-8 -*-

class Happy(object):
    _num_1 = 0
    _num_2 = 0
    num_output = 0

    def __init__(self, num_1, num_2):
        self._num_1 = int(num_1)
        self._num_2 = int(num_2)

    def Add(self):
        num_output = self._num_1 - self._num_2
        return num_output

    
if __name__ == '__main__':
    a = Happy(1, 2)
    print(a.Add())

