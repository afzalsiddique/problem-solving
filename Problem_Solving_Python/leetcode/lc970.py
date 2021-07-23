import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def create_pow_table(i):
            pows=[]
            x=1
            for _ in range(ENOUGH):
                pows.append(x)
                x*=i
                if x>bound: break
            return pows
        def get_power(num, pow): # num raised to pow
            if num==1: return 1
            if num==x:
                if pow>=len(pow_x):
                    return float('inf')
                return pow_x[pow]
            if num==y:
                if pow>=len(pow_y):
                    return float('inf')
                return pow_y[pow]

        ENOUGH = 21
        res=set()
        pow_x=create_pow_table(x)
        pow_y=create_pow_table(y)
        for i in range(ENOUGH):
            for j in range(ENOUGH):
                tmp=get_power(x,i)+get_power(y,j)
                if tmp<=bound:
                    res.add(tmp)
                else:
                    break
        return list(res)

class tester(unittest.TestCase):
    def test_1(self):
        x = 2
        y = 3
        bound = 10
        Output= [2,3,4,5,7,9,10]
        self.assertEqual(Output, sorted(get_sol().powerfulIntegers(x,y,bound)))
    def test_2(self):
        x = 3
        y = 5
        bound = 15
        Output= [2,4,6,8,10,14]
        self.assertEqual(Output, sorted(get_sol().powerfulIntegers(x,y,bound)))
    def test_3(self):
        x = 1
        y = 5
        bound = 1000000
        Output= [2, 6, 26, 126, 626, 3126, 15626, 78126, 390626]
        self.assertEqual(Output, sorted(get_sol().powerfulIntegers(x,y,bound)))
    def test_4(self):
        x = 1
        y = 1
        bound = 400000
        Output= [2]
        self.assertEqual(Output, sorted(get_sol().powerfulIntegers(x,y,bound)))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):