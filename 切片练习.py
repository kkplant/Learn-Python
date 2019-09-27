# -*- coding:utf-8 -*-

#def trim(s):
#   i = 0,
#   j = -1,
#    if s[:i+1] == " ":
#        i = i + 1
#    if s[j-1:] == " ":
#        j = j - 1
#    s = s[i:j]
#    return s

def trim(s):
    if s[:1] == ' ':
        return trim(s[:1])
    if s[-1:] == ' ':
        return trim(s[-1:])
    else:
        return s


print(trim('ab c  '))

