# -*- coding: utf-8 -*-
# User: ZhangWei
# Date: 2018/8/14 0014


class Npc(object):
    def __init__(self, hp):
        self._hp = hp

    def GetHp(self, SP, realHp):
        print ("My Hp is {}".format(realHp))


if __name__ == '__main__':
    Tom = Npc(1)
    Tom.GetHp(realHp=10, SP=None)
    from testsuites.al.modules.city.enemy import Enemy
    dog = Enemy(10, 5)
    dog.GetHp()
    dog.Attack()
    # Tom.Attack()
