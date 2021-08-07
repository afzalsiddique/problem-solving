import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n=len(l)
        res=[]
        for i in range(n):
            tmp=nums[l[i]:r[i]+1]
            sett1=set(tmp)
            minn=min(tmp)
            maxx=max(tmp)
            diff=(maxx-minn)/(r[i]-l[i])
            diff=int(diff)
            sett2=set()
            for j in range(r[i]-l[i]+1):
                sett2.add(minn+diff*j)
            if sett1==sett2:
                res.append(True)
            else:
                res.append(False)
        return res


class Tester(unittest.TestCase):
    def test_1(self):
        nums,l,r= [4,6,5,9,3,7],[0,0,2],[2,3,5]
        Output= [True,False,True]
        self.assertEqual(Output,get_sol().checkArithmeticSubarrays(nums,l,r))
    def test_2(self):
        nums,l,r= [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7],[4,4,9,7,9,10]
        Output= [False,True,False,False,True,True]
        self.assertEqual(Output,get_sol().checkArithmeticSubarrays(nums,l,r))
    def test_3(self):
        nums,l,r= [-3,-6,-8,-4,-2,-8,-6,0,0,0,0], [5,4,3,2,4,7,6,1,7], [6,5,6,3,7,10,7,4,10]
        Output= [True,True,True,True,False,True,True,True,True]
        self.assertEqual(Output,get_sol().checkArithmeticSubarrays(nums,l,r))
    def test_4(self):
        nums,l,r= [-3,-6,-8,-4,-2,-8,-6,0,0,0,0], [7,7], [10,10]
        Output= [True,True]
        self.assertEqual(Output,get_sol().checkArithmeticSubarrays(nums,l,r))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):