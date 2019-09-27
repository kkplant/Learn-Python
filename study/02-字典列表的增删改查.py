# -*- coding: utf-8 -*-
# User: ZhangWei
# Date: 2018/8/21 0021
#
#
# gem = {
#     "id": 80322,
#     "property": {
#         "exp": 640
#     },
#     "uniqueID": 181
# }
# a = gem["property"]["exp"]
# a = gem.get("id", 0)
#
# gem["buff"] = 100
# a = gem
#
# del gem["buff"]
# a = gem
#
# gem["id"] = 803444

# print a

gemList = {
    "a": {
        "id": 80322,
        "property": {
            "exp": 640
        },
        "uniqueID": 181
    },
    "b": {
        "id": 80313,
        "property": {
            "exp": 1280
        },
        "uniqueID": 182
    },
    "c": {
        "id": 80314,
        "property": {
            "exp": 1280
        },
        "uniqueID": 184
    },
}

# idIndex = 0
# idMaxGem = {}
# for perGem in gemList:
#     if perGem["id"] > idIndex:
#         idIndex = perGem["id"]
#         idMaxGem = perGem
# print idMaxGem

# gemList.append(gem)
# gemList.remove(gem)
gemList = gemList.values()
# gemList = gemList.keys()
# gemList = gemList.items()

print gemList
