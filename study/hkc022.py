def hundred(n):
    a = {}
    dic = a
    for i in range(1, n + 1):
        if i == n:
            dic[i] = "values"
        else:
            dic[i] = {}
            dic = dic[i]
    return a


num = hundred(100)
print ("a="),
print num


# def getNum(num):
#     val = 0
#     for i in range(1, 101):
#         val = num[i]
#     return val
# #
# #
# print getNum(num)

val = 0

for x in xrange(1, 101):
    num = num[x]
    if num is not dict:
        val = num
print val

