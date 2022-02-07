from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        intervals,res = [],[]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            start,end = -1 , -1
            for i in range(len(S)):
                if c==S[i]:
                    if start == -1:
                        start = i
                        end = i
                    else:
                        end = i
            if start!=-1:intervals.append([start,end])
        merged_intervals = self.merge(intervals)
        for start,end in merged_intervals:
            res.append(end-start+1)
        return res


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n==1: return intervals

        intervals.sort(key=lambda x:x[0])
        last_start, last_end = intervals[0][0], intervals[0][1]
        result = []
        for i in range(1,n):
            cur_start, cur_end = intervals[i][0],intervals[i][1]
            if cur_start>last_end:
                result.append([last_start,last_end])
                last_start = cur_start
            last_end = max(last_end, cur_end)
        result.append([last_start, last_end])
        return result

class MyTestCase(unittest.TestCase):
    def test001(self):
        self.assertEqual([9,7,8], get_sol().partitionLabels("ababcbacadefegdehijhklij"))
    def test002(self):
        self.assertEqual([10], get_sol().partitionLabels("eccbbbbdec"))
    def test01(self):
        self.assertEqual([[1,6],[8,10],[15,18]],get_sol().merge([[1,3],[2,6],[8,10],[15,18]]))
    def test02(self):
        self.assertEqual([[1,7],[8,10],[15,18]],get_sol().merge([[1,3],[2,6],[5,7],[8,10],[15,18]]))
    def test03(self):
        self.assertEqual([[1,5]],get_sol().merge([[1,4],[4,5]]))
    def test04(self):
        self.assertEqual([[0,4]],get_sol().merge([[1,4],[0,4]]))
    def test05(self):
        self.assertEqual([[1,4]],get_sol().merge([[1,4],[2,3]]))
    def test06(self):
        self.assertEqual([[1,10]],get_sol().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
