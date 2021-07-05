import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def reorderedPowerOf2(self, num: int) -> bool:
        a1=str(num)
        a1=sorted(a1)
        s1=a1[:]
        for i in range(32):
            a2 = str(1<<i)
            a2=sorted(a2)
            s2=a2[:]
            if s1==s2: return True
        return False
class Solution2:
    # tle
    def reorderedPowerOf2(self, num: int) -> bool:
        nums=[str(x) for x in str(num)]
        res=[]

        def search(n):
            l=0
            r=n//2
            while l<=r:
                mid = (l+r)//2
                tmp=2**mid
                if tmp==n: return True
                if tmp<n:
                    l=mid+1
                else:
                    r=mid-1
            return False

        def helper(nums:List[str],path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                x=nums[i]
                if not path and x=='0': continue
                nums.pop(i)
                helper(nums[:],path+[x])
                nums.insert(i,x)
                a=0

        helper(nums,[])
        # print(res)
        for x in res:
            x=int(''.join(x))
            if search(x): return True
        return False

class MyTestCase(unittest.TestCase):
    def test_01(self):
        n = 1
        Output= True
        self.assertEqual(Output,get_sol().reorderedPowerOf2(n))
    def test_02(self):
        n = 10
        Output= False
        self.assertEqual(Output,get_sol().reorderedPowerOf2(n))
    def test_03(self):
        n = 16
        Output= True
        self.assertEqual(Output,get_sol().reorderedPowerOf2(n))
    def test_04(self):
        n = 24
        Output= False
        self.assertEqual(Output,get_sol().reorderedPowerOf2(n))
    def test_05(self):
        n = 46
        Output= True
        self.assertEqual(Output,get_sol().reorderedPowerOf2(n))
    def test_06(self):
        n = 5792021
        Output= True
        self.assertEqual(Output,get_sol().reorderedPowerOf2(n))
    # def test_07(self):
    # def test_08(self):