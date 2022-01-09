import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/largest-multiple-of-three/discuss/518830/C%2B%2BJava-Concise-O(n)
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        d1=[1,4,7,2,5,8]
        d2=[2,5,8,1,4,7]
        count=Counter(digits)
        summ=sum(digits)
        while summ%3!=0:
            for d in d1 if summ%3==1 else d2:
                if count[d]:
                    summ-=d
                    count[d]-=1
                    break

        res=[]
        for i in range(9,-1,-1):
            while count[i]:
                res.append(str(i))
                count[i]-=1
        if not res:
            return ''
        if res[0]=='0':
            return '0'
        return ''.join(res)



class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('981', get_sol().largestMultipleOfThree([8,1,9]))
    def test_2(self):
        self.assertEqual('8760', get_sol().largestMultipleOfThree([8,6,7,1,0]))
    def test_3(self):
        self.assertEqual('', get_sol().largestMultipleOfThree([1]))
    def test_4(self):
        self.assertEqual('0', get_sol().largestMultipleOfThree([0,0,0,0,0,0]))
    def test_5(self):
        self.assertEqual('111', get_sol().largestMultipleOfThree([1,1,1]))
    def test_6(self):
        self.assertEqual('', get_sol().largestMultipleOfThree([5,8]))
    def test_7(self):
        self.assertEqual('966', get_sol().largestMultipleOfThree([9,8,6,8,6]))
    def test_8(self):
        self.assertEqual('966', get_sol().largestMultipleOfThree([9,7,6,7,6]))
