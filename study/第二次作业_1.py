# -*- coding: utf-8 -*-

playerInfo = {
    1: {'name': 'sam',
        'score': '10000'},
    2: {'name': 'lily',
        'score': '20000'},
    3: {'name': 'terry',
        'score': '15000'},
    4: {'name': 'michael',
        'score': '13555'}
}

i = 0
j = 0
score = 0
scoreMax = 0
for i in playerInfo:
    score = int(playerInfo[i].get('score')) 
    if score > scoreMax:
        scoreMax = score
        j = i
print(playerInfo[j].get('name'))
