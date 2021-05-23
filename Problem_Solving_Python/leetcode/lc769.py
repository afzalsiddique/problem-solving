import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/138844/Python-O(n)-Very-Detailed-Explanation
    # time O(n) space O(1)
    def maxChunksToSorted(self, arr):
        min_idx_for_chunk_end=-1
        chunks = 0
        for i, v in enumerate(arr):
            min_idx_for_chunk_end = max(min_idx_for_chunk_end, v)
            if min_idx_for_chunk_end==i:
                chunks+=1
        return chunks
class Solution2:
    # https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/113520/Java-solution-left-max-and-right-min.
    # time O(n) space O(n)
    def maxChunksToSorted(self, arr):
        n=len(arr)
        left_max=[float('-inf')]*n
        right_min=[float('inf')]*n
        cur_max=float('-inf')
        for i in range(n):
            if arr[i]>cur_max:
                cur_max=arr[i]
            left_max[i]=cur_max
        cur_min=float('inf')
        for i in reversed(range(n)):
            if arr[i]<cur_min:
                cur_min=arr[i]
            right_min[i]=cur_min
        print(left_max)
        print(right_min)
        chunks=1
        for i in range(n-1):
            if left_max[i]<=right_min[i+1]:
                chunks+=1
        if chunks>n: return n
        return chunks
class Solution3:
    # wrong
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        chunks=0
        cur_max=float('-inf')
        for i in range(n):
            if arr[i]>cur_max:
                cur_max=arr[i]
                chunks+=1
        return chunks

class tester(unittest.TestCase):
    def test01(self):
        arr = [4,3,2,1,0]
        Output= 1
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
    def test02(self):
        arr = [1,0,2,3,4]
        Output= 4
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
    def test03(self):
        arr = [1,2,0,3]
        Output= 2
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
    def test04(self):
        arr = [4,0,2,3,1]
        Output= 1
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
    def test05(self):
        arr = [0]
        Output= 1
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
    def test06(self):
        arr = [0,1]
        Output= 2
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
    def test07(self):
        arr = [0,2,1,4,3]
        Output= 3
        self.assertEqual(Output, get_sol().maxChunksToSorted(arr))
