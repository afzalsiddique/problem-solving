from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxx=1
        n = len(tree)
        di= {} # fruit_type, rightmost_index
        left,right = 0,0
        while right<n:
            if len(di)<2:
                di[tree[right]]=right
                right+=1
            elif len(di)==2 and tree[right] in di:
                di[tree[right]]=right
                right+=1
            else:
                if di[tree[left]]<=left:
                    di.pop(tree[left])
                left+=1
            maxx=max(maxx,right-left)
        return maxx



class tester(unittest.TestCase):
    def test01(self):
        Input= [1,2,1]
        Output= 3
        self.assertEqual(Output, get_sol().totalFruit(Input))
    def test02(self):
        Input= [0,1,2,2]
        Output= 3
        self.assertEqual(Output, get_sol().totalFruit(Input))
    def test03(self):
        Input= [1,2,3,2,2]
        Output= 4
        self.assertEqual(Output, get_sol().totalFruit(Input))
    def test04(self):
        Input= [3,3,3,1,2,1,1,2,3,3,4]
        Output= 5
        self.assertEqual(Output, get_sol().totalFruit(Input))
