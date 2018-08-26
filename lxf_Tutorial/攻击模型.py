# -*- coding:utf-8 -*-
#攻击、防御、生命、攻击间隔、攻击距离、移动速度
import math

att_attack=0
att_defend=0
att_life=0
att_interval=0
att_distance=0
att_speed=0

def_attack=0
def_defend=0
def_life=0
def_interval=0
def_distance=0
def_speed=0

Army_Infantry={'attack':1,'defend':2,'life':3,'interval':4,'distance':5,'speed':6}
Army_Archer={'attack':1,'defend':2,'life':3,'interval':4,'distance':5,'speed':6}
Army_Cavalry={'attack':1,'defend':2,'life':3,'interval':4,'distance':5,'speed':6}

print('请选择进攻方的兵种： \n 步兵：1 \n 弓兵：2 \n 骑兵：3')
Army_att=input('请输入进攻方兵种编号：')
print('请选择防守方的兵种： \n 步兵：1 \n 弓兵：2 \n 骑兵：3')
Army_def=input('请输入防守方兵种编号：')

if int(Army_att)==1:
    att_attack=Army_Infantry['attack']
    att_defend=Army_Infantry['defend']
    att_life=Army_Infantry['life']
    att_interval=Army_Infantry['interval']
    att_distance=Army_Infantry['distance']
    att_speed=Army_Infantry['speed']
elif int(Army_att)==2:
    att_attack=Army_Archer['attack']
    att_defend=Army_Archer['defend']
    att_life=Army_Archer['life']
    att_interval=Army_Archer['interval']
    att_distance=Army_Archer['distance']
    att_speed=Army_Archer['speed']  
elif int(Army_att)==3:
    att_attack=Army_Cavalry['attack']
    att_defend=Army_Cavalry['defend']
    att_life=Army_Cavalry['life']
    att_interval=Army_Cavalry['interval']
    att_distance=Army_Cavalry['distance']
    att_speed=Army_Cavalry['speed']
elif int(Army_def)==1:
    def_attack=Army_Infantry['attack']
    def_defend=Army_Infantry['defend']
    def_life=Army_Infantry['life']
    def_interval=Army_Infantry['interval']
    def_distance=Army_Infantry['distance']
    def_speed=Army_Infantry['speed']
elif int(Army_def)==2:
    def_attack=Army_Archer['attack']
    def_defend=Army_Archer['defend']
    def_life=Army_Archer['life']
    def_interval=Army_Archer['interval']
    def_distance=Army_Archer['distance']
    def_speed=Army_Archer['speed']
elif int(Army_def)==3:
    def_attack=Army_Cavalry['attack']
    def_defend=Army_Cavalry['defend']
    def_life=Army_Cavalry['life']
    def_interval=Army_Cavalry['interval']
    def_distance=Army_Cavalry['distance']
    def_speed=Army_Cavalry['speed']        
else:
    print('输入的兵种编号错误，无法计算。')
