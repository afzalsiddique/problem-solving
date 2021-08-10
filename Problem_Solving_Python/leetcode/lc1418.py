import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_items=set()
        di=defaultdict(Counter)
        for _,table,food in orders:
            di[int(table)][food]+=1
            food_items.add(food)
        food_items=sorted(list(food_items))
        res=[]
        res.append(['Table']+food_items)
        for table in sorted(di.keys()):
            tmp=[]
            for food in food_items:
                tmp.append(str(di[table][food]))
            res.append([str(table)]+tmp)
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
        Output= [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
        self.assertEqual(Output,get_sol().displayTable(orders))
    def test_2(self):
        orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
        Output= [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
        self.assertEqual(Output,get_sol().displayTable(orders))
    def test_3(self):
        orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
        Output= [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
        self.assertEqual(Output,get_sol().displayTable(orders))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):