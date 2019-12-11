#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/11/23 21:31
#@Author :zbwu103
#@File  ：1.py
#@功能：

import shelve

db = shelve.open('persondb')

print(list(db.keys()))

for key in db:
    print(key,'=>',db[key])


sue=db['Sue Jones']
sue.giveRaise(0.1)
print(sue.pay)
db['Sue Jones']=sue
db.close()