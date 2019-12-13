# -*- coding:utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test_sqlite.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', '95')")
cursor.execute(r"insert into user values ('A-002', 'Bart', '62')")
cursor.execute(r"insert into user values ('A-003', 'Lisa', '78')")
cursor.close()
conn.commit()
conn.close()

#根据分数段查找指定名字
def get_score_in(low, high):
    '返回指定分数区间的名字，按分数从低到高排序'
    import sqlite3
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select name from user where score>=? and score<=? order by score', (low, high))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    result = []
    for i in values:
        result.append(i[0])
    return result

#测试
print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60, 100))
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('Test Pass')
