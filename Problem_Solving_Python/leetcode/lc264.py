from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # time O(n) space O(n)
    # any ugly number is some other ugly number,
    def nthUglyNumber(self, n: int) -> int:
        dp=[0]*n
        dp[0]=1
        p2,p3,p5=0,0,0
        for i in range(1,n):
            tmp2=dp[p2]*2
            tmp3=dp[p3]*3
            tmp5=dp[p5]*5
            dp[i]=min(tmp2,tmp3,tmp5)
            if dp[i]==tmp2:
                p2+=1
            if dp[i]==tmp3:
                p3+=1
            if dp[i]==tmp5:
                p5+=1
        return dp[-1]
class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        s = set()
        cnt = 0
        while cnt!=n:
            temp = heappop(heap)
            if temp in s:
                continue
            s.add(temp)
            heappush(heap,temp*2)
            heappush(heap,temp*3)
            heappush(heap,temp*5)
            cnt+=1
        return temp

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(12, get_sol().nthUglyNumber(10))
    def test02(self):
        self.assertEqual(1, get_sol().nthUglyNumber(1))
    def test03(self):
        self.assertEqual(2, get_sol().nthUglyNumber(2))
    def test04(self):
        self.assertEqual(3, get_sol().nthUglyNumber(3))
    def test05(self):
        self.assertEqual(4, get_sol().nthUglyNumber(4))
    def test06(self):
        self.assertEqual(5, get_sol().nthUglyNumber(5))
    def test07(self):
        self.assertEqual(6, get_sol().nthUglyNumber(6))
    def test08(self):
        self.assertEqual(8, get_sol().nthUglyNumber(7))

