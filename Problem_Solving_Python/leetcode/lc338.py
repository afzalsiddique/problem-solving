from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i&(i-1)]+1 # turn off the last set bit and add 1
        return dp
class Solution3:
    def countBits(self, num: int) -> List[int]:
        def divide(num):
            if num==0:return 0,0
            cnt = 0
            temp = num
            while temp!=1:
                temp=temp//2
                cnt+=1
            while cnt:
                temp = temp*2
                cnt-=1
            return temp, num-temp

        def init_dp_array(num):
            dp = [0] * (num + 1)
            i=1
            while i<=num:
                dp[i]=1
                i*=2
            return dp

        dp = init_dp_array(num)
        for i in range(num+1):
            idx1,idx2 = divide(i)
            dp[i] = dp[idx1]+dp[idx2]
        return dp
class Solution2:
    def countBits(self, n: int) -> List[int]:
        def countSetBits(mask): return 0 if mask==0 else 1+countSetBits(mask&(mask-1))

        return [countSetBits(i) for i in range(n+1)]
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([0,1,1],get_sol().countBits(2))
    def test02(self):
        self.assertEqual([0, 1, 1, 2, 1, 2],get_sol().countBits(5))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
