import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n=len(nums1),len(nums2)
        res=[]
        pq=[]
        for i in range(m):
            a,b=nums1[i],nums2[0]
            heappush(pq,[a+b,a,b,0]) # [sum(key for heap), a,b,idx of nums2]
        while len(res)!=k and pq:
            _,a,b,idx=heappop(pq)
            res.append([a,b])
            idx+=1 # make pair of next number of nums2 and a
            if idx==len(nums2): continue
            new_b=nums2[idx]
            heappush(pq,[a+new_b,a,new_b,idx])
        return res
class Solution2:
    # not good in terms of memory
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n = len(nums1), len(nums2)
        if n*m < k:
            return sorted([[a, b] for b in nums2 for a in nums1])
        heap = []
        for j in range(n):
            heap.append([nums1[0]+nums2[j],nums1[0],nums2[j]])
        heapify(heap)

        res = []
        i = 0
        while i!=k:
            res.append(heappop(heap)[1:3])
            i+=1
            if i<m:
                for j in range(n):
                    heappush(heap, [nums1[i]+nums2[j],nums1[i],nums2[j]])
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = get_sol().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
        self.assertEqual([[1,2],[1,4],[1,6]], actual)
    def test_2(self):
        expected = [[1,1],[1,1]]
        actual = get_sol().kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)
        self.assertEqual(expected, actual)
    def test_3(self):
        expected = [[1,3],[2,3]]
        actual = get_sol().kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3)
        self.assertEqual(expected, actual)
    def test_4(self):
        expected = [[1,3],[2,3],[1,5]]
        actual = get_sol().kSmallestPairs(nums1 = [1,2,4,5,6], nums2 = [3,5,7,9], k = 3)
        self.assertEqual(expected, actual)
