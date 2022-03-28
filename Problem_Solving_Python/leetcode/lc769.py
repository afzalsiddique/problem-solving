from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
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
    # time O(n) space O(n)
    def maxChunksToSorted(self, arr: List[int]) -> int:
        left_max=list(accumulate(arr,max))
        right_min=list(accumulate(arr[::-1],min))[::-1]
        chunks=1
        for i in range(len(arr)-1):
            if left_max[i]<right_min[i+1]:
                chunks+=1
        return chunks
class Solution4:
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


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().maxChunksToSorted([0]))
    def test02(self):
        self.assertEqual(2, get_sol().maxChunksToSorted([0,1]))
    def test03(self):
        self.assertEqual(2, get_sol().maxChunksToSorted([0,2,1]))
    def test04(self):
        self.assertEqual(2, get_sol().maxChunksToSorted([1,2,0,3]))
    def test05(self):
        self.assertEqual(1, get_sol().maxChunksToSorted([4,3,2,1,0]))
    def test06(self):
        self.assertEqual(4, get_sol().maxChunksToSorted([1,0,2,3,4]))
    def test07(self):
        self.assertEqual(1, get_sol().maxChunksToSorted([4,0,2,3,1]))
    def test08(self):
        self.assertEqual(3, get_sol().maxChunksToSorted([0,2,1,4,3]))
