# -*- coding: utf-8 -*-
# User: ZhangWei
# Date: 2018/8/23 0023
from testsuites.al.modules.city import Npc


class Enemy(Npc):
    def __init__(self, hp, att):
        super(Enemy, self).__init__(hp)
        self.att = att

    def Attack(self):
        print ("Damage:{}".format(self.att))
