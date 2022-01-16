import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @functools.lru_cache(None)
        def recurse(target):
            # print(target)
            if x > target:
                option1=target * 2 - 1   # x=5,t=3 -> 5/5+5/5+5/5
                option2=(x - target) * 2 # x=5,t=3 -> 5-5/5-5/5
                return min(option1,option2)
            if x==target:
                return 0

            cnt=0
            product=x
            while product<target:
                product*=x
                cnt+=1
            if product==target:
                return cnt
            option1,option2=float('inf'),float('inf')
            # option1: in the form : x*x*...*x - (......) = target. Here product>target. So we need to subtract
            if product-target<target: # avoid infinite loop
                option1=cnt+1+recurse(product-target) # +1 for subtraction operator

            # option2: in the form : x*x*...*x + (......) = target. Here product>target. Make product less than target. Then we need to add
            product//=x # Now product < target
            cnt-=1
            option2=cnt+1+recurse(target-product) # +1 for addition operator
            return min(option1,option2)

        return recurse(target)
class Solution2:
    # tle
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def eval(li):
            st=[x]
            for c in li:
                if c=='+':
                    st.append(x)
                elif c=='-':
                    st.append(x*(-1))
                elif c=='*':
                    st.append(st.pop()*x)
                else:
                    st.append(int(st.pop()/x))
            return sum(st)==target

        q=deque()
        q.append([])
        while q:
            li=q.popleft()
            if eval(li):
                return len(li)
            for c in '+-/*':
                q.append(li+[c])


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5,get_sol().leastOpsExpressTarget(3, 19))
    def test2(self):
        self.assertEqual(8,get_sol().leastOpsExpressTarget(5, 501))
    def test3(self):
        self.assertEqual(3,get_sol().leastOpsExpressTarget(100, 100000000))
    def test4(self):
        self.assertEqual(17,get_sol().leastOpsExpressTarget(3, 365))
    def test5(self):
        self.assertEqual(4,get_sol().leastOpsExpressTarget(2,12))
    def test6(self):
        self.assertEqual(7,get_sol().leastOpsExpressTarget(11,187))
    def test7(self):
        self.assertEqual(104,get_sol().leastOpsExpressTarget(2, 6125100))
    def test8(self):
        self.assertEqual(41,get_sol().leastOpsExpressTarget(11, 500041))
