#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Author:lthan
# @Email :xiaohan809@qq.com
# @Time  :2018/1/19 11:59
from sort.topK import *
tk = TopKHeap(lambda x,y:x < y)
bk = BtmKHeap(lambda x,y:x < y)
sq = [1,25567,1,3,2,-1,1,-1,1,2,3,4,5,6,7,8,9,10,11,234,12,25567,25567,22]
print tk.run(sq,5)
print bk.run(sq,5)
qs = QuickSelect(lambda x,y:(x - y))
print qs.run(sq,5)
qs = QuickSelect(lambda x,y:-(x - y))
print qs.run(sq,5)