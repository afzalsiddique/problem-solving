import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self):
        super().__init__()
        self.data = []
    def top(self): return -self.data[0]
    def topPrice(self): return -self.data[0][0]
    def topAmount(self): return -self.data[0][1]
    def setTopAmount(self,val): self.data[0][1]=val*(-1)
    def push(self, val1,val2): heappush(self.data, [-val1,-val2])
    def heappop(self): return heappop(self.data)
    def __repr__(self): return str(self.data)
    def __bool__(self): return True if len(self.data) else False
class MinHeap(list):
    def __init__(self):
        super().__init__()
        self.data = []
    def top(self): return self.data[0]
    def topPrice(self): return self.data[0][0]
    def topAmount(self): return self.data[0][1]
    def setTopAmount(self,val): self.data[0][1]=val
    def push(self, val1,val2): heappush(self.data, [val1,val2])
    def heappop(self): return heappop(self.data)
    def __repr__(self): return str(self.data)
    def __bool__(self): return True if len(self.data) else False
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9+7
        sell = MinHeap()
        buy = MaxHeap()
        for price,amount,type in orders:
            if type==0: # buy
                while sell and sell.topPrice()<=price and amount:
                    minn = min(sell.topAmount(),amount)
                    amount -= minn
                    sell.setTopAmount(sell.topAmount()-minn)
                    if not sell.topAmount():
                        sell.heappop()
                if amount:
                    buy.push(price,amount)
            else:
                while buy and buy.topPrice()>=price and amount:
                    minn = min(buy.topAmount(),amount)
                    amount -= minn
                    buy.setTopAmount(buy.topAmount()-minn)
                    if not buy.topAmount():
                        buy.heappop()
                if amount:
                    sell.push(price,amount)
            # print(buy)
            # print(sell)
            # print()

        buy_amount = sum(-x[1] for x in buy.data) % MOD
        sell_amount = sum(x[1] for x in sell.data) % MOD
        # print('buy:',buy_amount,' sell:', sell_amount)
        return (sell_amount + buy_amount) % MOD
class Solution2:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        for price, amount, orderType in orders :
            if orderType == 0 : # buy
                while amount > 0 and len(sell) > 0 :
                    pt = sell[0]
                    if pt[0] > price :
                        break
                    deal = min(amount, pt[1])
                    amount -= deal
                    pt[1] -= deal
                    if pt[1] == 0 :
                        heappop(sell)
                if amount > 0 :
                    heappush(buy, [-price, amount])
            else : # sell
                while amount > 0 and len(buy) > 0 :
                    pt = buy[0]
                    if -pt[0] < price :
                        break
                    deal = min(amount, pt[1])
                    amount -= deal
                    pt[1] -= deal
                    if pt[1] == 0 :
                        heappop(buy)
                if amount > 0 :
                    heappush(sell, [price, amount])
        res = sum([t[1] for t in buy]) + sum([t[1] for t in sell])
        return res % (10**9+7)



class MyTestCase(unittest.TestCase):
    def test1(self):
        orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
        Output= 6
        self.assertEqual(Output, get_sol().getNumberOfBacklogOrders(orders))
    def test2(self):
        orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
        Output= 999999984
        self.assertEqual(Output, get_sol().getNumberOfBacklogOrders(orders))
    # def test3(self):
    # def test4(self):
