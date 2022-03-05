from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            li=[]
            for c in str(num):
                li.append(str(mapping[int(c)]))
            return int(''.join(li))

        n=len(nums)
        li=[[convert(nums[i]),i] for i in range(n) ]
        li.sort()
        return [nums[i] for _,i in li]



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([338,38,991], get_sol().sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))
    def test02(self):
        self.assertEqual([123,456,789], get_sol().sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]))
    # def test03(self):
    # def test04(self):
