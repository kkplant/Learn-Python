# -*- coding: utf-8 -*-

# l = [1, 3, 4, 1, 5, 7]
# j = -1
# for i in l:
#     j += 1
#     if i % 2 == 0:
#         l.pop(j)
#         print l
#         print i

l = [4, 3, 2, 4, 1, 5, 4, 7]
l1 = []
for i in l:
    if i % 2 != 0:
        l1.append(i)
l = l1
print l

