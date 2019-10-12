# -*- coding:utf-8 -*-
# User:chenxiong

class Lottery:
    def __init__(self):
        self._numbers1 = []
        self._numbers2 = []

    def LotteryChoice(self):
        import random
        from datetime import date

        i = 1
        j = 1
        while i < 6:
            self._numbers1.append(random.sample(range(1,36), 1))
            i = i + 1
        
        while j < 3:
            self._numbers2.append(random.sample(range(1,13), 1))
            j = j + 1
        
        print(date.today())
        print('%s + %s' %(self._numbers1, self._numbers2))
        
l = Lottery()
l.LotteryChoice()
        
        
