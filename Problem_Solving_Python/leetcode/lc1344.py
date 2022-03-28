from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h=(hour*5+(minutes/60)*5)%60
        option1=abs(h-minutes)
        option2=abs(minutes+60-h)
        option3=abs(minutes-(h+60))
        space=min(option1,option2,option3)
        return space/60*360

class MyTestCase(unittest.TestCase):
    def test1(self):
        hour,minutes = 12,  30
        Output= 165
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test2(self):
        hour,minutes = 3,  30
        Output= 75
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test3(self):
        hour,minutes = 3,  15
        Output= 7.5
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test4(self):
        hour,minutes = 4,  50
        Output= 155
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test5(self):
        hour,minutes = 12,  0
        Output= 0
        self.assertEqual(Output, get_sol().angleClock(hour,minutes))
    def test6(self):
        self.assertEqual(76.5,get_sol().angleClock(1,57))
