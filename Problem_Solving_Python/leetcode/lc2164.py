from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n=len(nums)
        even=[]
        odd=[]
        res=[]
        for i,x in enumerate(nums):
            if i%2==0:
                even.append(x)
            else:
                odd.append(x)
        even.sort(reverse=True)
        odd.sort()
        for i in range(n):
            if i%2==0:
                res.append(even.pop())
            else:
                res.append(odd.pop())
        return res



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([2,3,4,1], get_sol().sortEvenOdd([4,1,2,3]))
    def test02(self):
        self.assertEqual([2,1], get_sol().sortEvenOdd([2,1]))
    # def test03(self):
    #     self.assertEqual(, get_sol().())
    # def test04(self):
    #     self.assertEqual(, get_sol().())
