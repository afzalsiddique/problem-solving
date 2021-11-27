import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        di = defaultdict(lambda : defaultdict(set))
        for tran in transactions:
            name,time,amount,city = tran.split(',')
            time,amount = int(time),int(amount)
            di[time][name].add(city)

        for tran in transactions:
            name,time,amount,city = tran.split(',')
            time,amount = int(time),int(amount)
            if amount>1000:
                res.append(tran)
                continue
            for t in range(time-60,time+61):
                if name not in di[t]: continue
                cities = di[t][name]
                if city not in cities or len(cities)>1:
                    res.append(tran)
                    break

        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
        Output= ["alice,20,800,mtv","alice,50,100,beijing"]
        self.assertEqual(Output, get_sol().invalidTransactions(transactions))
    def test2(self):
        transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
        Output= ["alice,50,1200,mtv"]
        self.assertEqual(Output, get_sol().invalidTransactions(transactions))
    def test3(self):
        transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
        Output= ["bob,50,1200,mtv"]
        self.assertEqual(Output, get_sol().invalidTransactions(transactions))
    def test4(self):
        transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
        Output= ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
        self.assertEqual(Output, get_sol().invalidTransactions(transactions))
    def test5(self):
        transactions = ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
        Output= ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
        self.assertEqual(Output, get_sol().invalidTransactions(transactions))
    def test6(self):
        transactions = ["alice,20,800,mtv","alice,50,1200,mtv","alice,50,100,beijing"]
        Output= ["alice,20,800,mtv","alice,50,1200,mtv","alice,50,100,beijing"]
        self.assertEqual(Output, get_sol().invalidTransactions(transactions))
    # def test7(self):
