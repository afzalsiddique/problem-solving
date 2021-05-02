import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
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



def get_sol_obj():
    return Solution()
class tester(unittest.TestCase):
    def test01(self):
        Input= [1,2,1]
        Output= 3
        self.assertEqual(Output,get_sol_obj().totalFruit(Input))
    def test02(self):
        Input= [0,1,2,2]
        Output= 3
        self.assertEqual(Output,get_sol_obj().totalFruit(Input))
    def test03(self):
        Input= [1,2,3,2,2]
        Output= 4
        self.assertEqual(Output,get_sol_obj().totalFruit(Input))
    def test04(self):
        Input= [3,3,3,1,2,1,1,2,3,3,4]
        Output= 5
        self.assertEqual(Output,get_sol_obj().totalFruit(Input))
