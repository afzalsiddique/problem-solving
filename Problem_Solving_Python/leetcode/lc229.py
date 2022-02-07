from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=yDbkQd9t2ig
class Solution:
    def majorityElement(self, nums) -> List[int]:
        cand1,cand2=0,0
        ahead1=0 # ahead1 means how many votes ahead person1 is from 3rd most voted person
        ahead2=0 # ahead2 means how many votes ahead person2 is from 3rd most voted person
        res=[]
        for num in nums:
            if num==cand1:
                ahead1+=1
            elif num==cand2:
                ahead2+=1
            else:
                if ahead1==0:
                    cand1=num
                    ahead1+=1
                elif ahead2==0:
                    cand2=num
                    ahead2+=1
                else:
                    ahead1-=1
                    ahead2-=1
        cnt1,cnt2=0,0
        for num in nums:
            if num==cand1:
                cnt1+=1
            elif num==cand2:
                cnt2+=1
        if cnt1>len(nums)//3:res.append(cand1)
        if cnt2>len(nums)//3:res.append(cand2)
        return res
class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1,maj2,cnt1,cnt2=0,0,0,0
        for num in nums:
            if num in [maj1,maj2]:
                if num==maj1:
                    cnt1+=1
                else:
                    cnt2+=1
            else:
                if cnt1 == 0 or cnt2==0:
                    if cnt1==0:
                        maj1 = num
                        cnt1+=1
                    elif cnt2==0:
                        maj2 = num
                        cnt2+=1
                else:
                    cnt1-=1
                    cnt2-=1
        cnt1, cnt2=0,0
        for num in nums:
            if num == maj1: cnt1+=1
            elif num == maj2: cnt2+=1
        res,n = [],len(nums)
        if cnt1>n//3: res.append(maj1)
        if cnt2>n//3: res.append(maj2)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(['a','c'],get_sol().majorityElement(['a','a','a','a','b','b','b','c','c','c','c']))
    def test2(self):
        self.assertEqual([],get_sol().majorityElement(['a','a','a','a','b','b','b','c','c','c','c','d','d','d','d','d']))
    def test_1(self):
        solution = Solution()
        nums = [3,2,3]
        actual = solution.majorityElement(nums)
        expected = [3]
        self.assertEqual(expected, actual)
    def test_2(self):
        nums = [1]
        actual = get_sol().majorityElement(nums)
        expected = [1]
        self.assertEqual(expected, actual)
    def test_3(self):
        nums = [1,2]
        actual = get_sol().majorityElement(nums)
        expected = [1,2]
        self.assertEqual(expected, actual)
    def test_4(self):
        nums = [2,2,1,3]
        actual = get_sol().majorityElement(nums)
        expected = [2]
        self.assertEqual(expected, actual)
    def test_5(self):
        nums = [1,1,2,2,7,7,8,8,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3]
        actual = get_sol().majorityElement(nums)
        expected = [9,3]
        self.assertEqual(expected, actual)
    def test_6(self):
        a=[8,8,9,3,9,3,9,3,9,3,9,3,9,3,]
        self.assertEqual(get_sol().majorityElement(a),get_sol().majorityElement(a))
