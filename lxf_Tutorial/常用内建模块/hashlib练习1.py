# -*- coding:utf-8 -*-

db_login = {}
'''
添加合法输入验证
'''
key_login =input('请输入用户名：')
value_login = input('请输入登录密码：')

def calc_md5(password):
    import hashlib
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

db_login[key_login] = calc_md5(value_login)
print(db_login)