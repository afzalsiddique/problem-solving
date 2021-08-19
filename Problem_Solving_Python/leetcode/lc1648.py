import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927674/Python3-Greedy
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def sumRange(lo, hi): # inclusive lo and hi
            return (hi * (hi+1)) // 2 - (lo * (lo-1)) // 2
        n=len(inventory)
        inventory.sort(reverse=True)
        inventory.append(0) # avoid out of range
        profit = 0
        width = 1 # width only increases. width is the count of first number from the left
                    # 10 | 8 | 6 | 4 | 2   width=1
                    #  8 | 8 | 6 | 4 | 2   width=2
                    #  6 | 6 | 6 | 4 | 2   width=3
                    #  4 | 4 | 4 | 4 | 2   width=4
                    #  2 | 2 | 2 | 2 | 2   width=5
                    #  0 | 0 | 0 | 0 | 0   width=5

        for i in range(n):
            if inventory[i] > inventory[i+1]:
                if width * (inventory[i] - inventory[i+1]) < orders:
                    profit += width * sumRange(inventory[i+1]+1, inventory[i])
                    orders -= width * (inventory[i] - inventory[i+1])
                else:
                    whole, remaining = divmod(orders, width)
                    profit += width * sumRange(inventory[i]-whole+1, inventory[i])
                    profit += remaining * (inventory[i]-whole)
                    break
            width += 1
        return profit % (10**9 + 7)



class MyTestCase(unittest.TestCase):
    def test_1(self):
        inventory,orders = [2,5],4
        Output= 14
        self.assertEqual(Output, get_sol().maxProfit(inventory,orders))
    def test_2(self):
        inventory,orders = [3,5],6
        Output= 19
        self.assertEqual(Output, get_sol().maxProfit(inventory,orders))
    def test_3(self):
        inventory,orders = [2,8,4,10,6],20
        Output= 110
        self.assertEqual(Output, get_sol().maxProfit(inventory,orders))
    def test_4(self):
        inventory,orders = [1000000000],1000000000
        Output= 21
        self.assertEqual(Output, get_sol().maxProfit(inventory,orders))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):