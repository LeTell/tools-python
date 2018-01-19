#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Author:lthan
# @Email :xiaohan809@qq.com
# @Time  :2018/1/19 11:53

import heapq
class QuickSelect(object):
    '''
    快选排序
    '''
    def __init__(self,compare_func):
        self.compare = compare_func
    def __partition(self,seq):
        mid,seq = seq[0],seq[1:]
        low = [x for x in seq if self.compare(x,mid) <= 0]
        high = [x for x in seq if not self.compare(x,mid) <= 0]
        return low,mid,high
    def run(self,seq,k):
        if len(seq) == 0 or len(seq) <= k:
            return seq
        low,mid,high = self.__partition(seq)
        if len(low) == k:
            return low
        if len(low) < k:
            low.append(mid)
            if len(low) == k:
                return low
            return low + self.run(high,k-len(low))
        return self.run(low,k)

class TopKHeap(object):
    '''
    小顶堆排序，适合无重复数据，获取最大的topK个值
    '''
    def __init__(self,compare_func):
        self.compare = compare_func
        self.data = []
    def __push(self,elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data,elem)
        else:
            top = self.data[0]

            if self.compare(top,elem):
                heapq.heapreplace(self.data,elem)
    def run(self,seq,k):
        assert type(k) == int,"参数k需要为int类型"
        self.k = k
        for val in seq:
            self.__push(val)
        return self.data

class BtmKHeap(object):
    '''
    大顶堆排序，适合无重复数据，获取最小的bottomK个值
    '''
    def __init__(self,compare_func):
        self.compare = compare_func
        self.data = []
    def __push(self,elem):
        elem = -elem
        if len(self.data) < self.k:
            heapq.heappush(self.data,elem)
        else:
            top = self.data[0]
            if self.compare(top,elem):
                heapq.heapreplace(self.data,elem)

    def run(self,seq,k):
        assert type(k) == int,"参数k需要为int类型"
        self.k = k
        for val in seq:
            self.__push(val)
        return sorted([-x for x in self.data])

# tk = TopKHeap(lambda x,y:x < y)
# bk = BtmKHeap(lambda x,y:x < y)
# sq = [1,25567,1,3,2,-1,1,-1,1,2,3,4,5,6,7,8,9,10,11,234,12,25567,25567,22]
# print tk.run(sq,5)
# print bk.run(sq,5)
# qs = QuickSelect(lambda x,y:(x - y))
# print qs.run(sq,5)
# qs = QuickSelect(lambda x,y:-(x - y))
# print qs.run(sq,5)