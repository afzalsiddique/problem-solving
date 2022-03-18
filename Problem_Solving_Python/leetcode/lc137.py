from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=cOFAmaMBVps&t=249s
    # In python if you has a positive integer, you can't get negative integer by setting its highest bit to 1 because
    # there is no highest bit actually. Int in python is an object and has no upper limit, you could try 1<<31,
    # you get 2147483648 other than -2147483648
    def convert(self,x):
        # unsigned value of -4 = 4294967292
        # return 4294967292-2^32 which is equal to -4
        if x >= 2**31:
            x -= 2**32
        return x
    def singleNumber(self, nums: List[int]) -> int:
        ans,shift=0,1
        for i in range(32):
            cnt=0
            for num in nums:
                if (num>>i) & 1:
                    cnt+=1
            if cnt%3:
                ans+=shift # ans|=shift also works
            shift=shift<<1
        return self.convert(ans)

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,get_sol().singleNumber([2,2,3,2]))
    def test2(self):
        self.assertEqual(-4,get_sol().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
    def test7(self):
        self.assertEqual(2,get_sol().convert(4294967298))
    def test6(self):
        self.assertEqual(1,get_sol().convert(4294967297))
    def test3(self):
        self.assertEqual(0,get_sol().convert(4294967296))
    def test4(self):
        self.assertEqual(-1,get_sol().convert(4294967295))
    def test5(self):
        self.assertEqual(-2,get_sol().convert(4294967294))
