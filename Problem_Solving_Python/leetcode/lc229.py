from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()

# a non-majority element can not cancel a majority element
class Solution:
    def majorityElement(self, A: List[int]) -> List[int]:
        n=len(A)
        if n==1: return [A[0]]
        cand=[A[0],A[0]]
        cnt=[0,0]
        for x in A:
            if x==cand[0]:
                cnt[0]+=1
            elif x==cand[1]:
                cnt[1]+=1
            elif cnt[0]==0:
                cand[0]=x
                cnt[0]=1
            elif cnt[1]==0:
                cand[1]=x
                cnt[1]=1
            else:
                cnt[0]-=1
                cnt[1]-=1

        # print(n)
        # print(Counter(A))
        # print(cand)
        # print(cnt)
        cnt[0]=sum(x==cand[0] for x in A)
        cnt[1]=sum(x==cand[1] for x in A)
        if cand[0]==cand[1]:
            cand.pop()
        return [x for i,x in enumerate(cand) if cnt[i]>n//3]
# https://www.youtube.com/watch?v=yDbkQd9t2ig
class Solution2:
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
    def test11(self):
        self.assertEqual(['a','c'],get_sol().majorityElement(['a','a','a','a','b','b','b','c','c','c','c']))
    def test12(self):
        self.assertEqual([],get_sol().majorityElement(['a','a','a','a','b','b','b','c','c','c','c','d','d','d','d','d']))
    def test01(self):
        self.assertEqual([3], get_sol().majorityElement([3,2,3]))
    def test02(self):
        self.assertEqual([1], get_sol().majorityElement([1]))
    def test03(self):
        self.assertEqual([1,2], get_sol().majorityElement([1,2]))
    def test04(self):
        self.assertEqual([2], get_sol().majorityElement([2,2,1,3]))
    def test05(self):
        self.assertEqual([9,3], get_sol().majorityElement([1,1,2,2,7,7,8,8,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9,3]))
    def test06(self):
        self.assertEqual([3,9], get_sol().majorityElement([8,8,9,3,9,3,9,3,9,3,9,3,9,3,]))
    def test07(self):
        self.assertEqual([2],get_sol().majorityElement([2,2]))
