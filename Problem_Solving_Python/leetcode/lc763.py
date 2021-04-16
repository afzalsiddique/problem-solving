from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



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

class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual([9,7,8], Solution().partitionLabels("ababcbacadefegdehijhklij"))