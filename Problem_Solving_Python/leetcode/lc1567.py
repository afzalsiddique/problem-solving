import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # counting negative signs
    def getMaxLen(self, nums: List[int]) -> int:
        def h(nums):
            n=len(nums)
            prev_idx=-1
            neg=0
            maxx=0
            for i in range(n):
                if nums[i]==0:
                    prev_idx=i
                    neg=0
                elif nums[i]<0:
                    neg+=1
                if not neg&1:
                    maxx=max(maxx,i-prev_idx)
            return maxx
        return max(h(nums), h(nums[::-1]))
class Solution2:
    # similar 1524
    # see array version for visualization below
    def getMaxLen(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[0]>0:
            pos=1
            neg=0
        elif nums[0]<0:
            pos=0
            neg=1
        else:
            pos=0
            neg=0
        maxx=pos
        for i in range(1,n):
            prev_neg=neg
            prev_pos=pos
            if nums[i]>0:
                if prev_neg:
                    neg=prev_neg+1
                else:
                    neg=0
                pos=prev_pos+1
            elif nums[i]<0:
                neg=prev_pos+1
                if prev_neg:
                    pos=prev_neg+1
                else:
                    pos=0
            else:
                pos=0
                neg=0
            maxx=max(maxx,pos)
        return maxx
class Solution2:
    def getMaxLen(self, nums: List[int]) -> int:
        n=len(nums)
        neg=[0]*n
        pos=[0]*n
        if nums[0]>0:
            pos[0]=1
            neg[0]=0
        elif nums[0]<0:
            pos[0]=0
            neg[0]=1
        else:
            pos[0]=0
            neg[0]=0
        for i in range(1,n):
            if nums[i]>0:
                if neg[i-1]:
                    neg[i]=neg[i-1]+1
                else:
                    neg[i]=0
                pos[i]=pos[i-1]+1
            elif nums[i]<0:
                neg[i]=pos[i-1]+1
                if neg[i-1]:
                    pos[i]=neg[i-1]+1
                else:
                    pos[i]=0
            else:
                pos[i]=0
                neg[i]=0
        # print(neg)
        # print(pos)
        return max(pos)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,-2,-3,4]
        Output= 4
        self.assertEqual(Output, get_sol().getMaxLen(nums))
    def test_2(self):
        nums = [0,1,-2,-3,-4]
        Output= 3
        self.assertEqual(Output, get_sol().getMaxLen(nums))
    def test_3(self):
        nums = [-1,-2,-3,0,1]
        Output= 2
        self.assertEqual(Output, get_sol().getMaxLen(nums))
    def test_4(self):
        nums = [-1,2]
        Output= 1
        self.assertEqual(Output, get_sol().getMaxLen(nums))
    def test_5(self):
        nums = [1,2,3,5,-6,4,0,10]
        Output= 4
        self.assertEqual(Output, get_sol().getMaxLen(nums))
    def test_6(self):
        nums = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
        Output= 8
        self.assertEqual(Output, get_sol().getMaxLen(nums))
