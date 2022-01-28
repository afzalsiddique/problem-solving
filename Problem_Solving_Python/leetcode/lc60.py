from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n):
            return n*fact(n-1) if n!=0 else 1

        k-=1
        res = []
        nums=[x for x in range(1,n+1)]
        while len(nums)>0:
            f = fact(len(nums)-1)
            idx = k//f
            res.append(nums[idx])
            nums.pop(idx)
            k=k%f
            # k=k-(k//f)*f # also works
        res = map(str,res)
        return ''.join(res)
class Solution2:
    def getPermutation(self, n: int, k: int):
        def factorial(x):
            return x*factorial(x-1) if x!=0 else 1
    
        k-=1
        b,ans,res = 0,0,[]
        nums=[i for i in range(1,n+1)]
        for i in reversed(range(n)):
            k -= b*ans
            b = factorial(i)
            ans = k//b
            # print(i,k,b,ans)
            res.append(nums[ans])
            nums = nums[:ans] + nums[ans+1:]
    
        return "".join([str(x) for x in res])

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.getPermutation(3,3)
        expected = '213'
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.getPermutation(4,9)
        expected = '2314'
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.getPermutation(5,60)
        expected = '32541'
        self.assertEqual(expected, actual)

