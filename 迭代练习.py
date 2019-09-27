# -*- coding:utf-8 -*-

def findMinAndMax(list):
    if len(list) == 0:
        return ('NONE','NONE')
    elif len(list) == 1:
        return list
    else:
        Min,Max = list[0],list[0]
        for i in list:
            if Min > i:
                Min = i
            if Max < i:
                Max = i
        return (Min,Max)


print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7,1]))
print(findMinAndMax([7,1,3,5,9]))

