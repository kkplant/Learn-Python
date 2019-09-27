# -*- coding: utf-8 -*-
xDict = {}
i = 1
while i < 3:
    xDict[xDict[i]] = xDict
    i += 1
print(xDict)
#xDict[i] = xDict
#print(xDict)

