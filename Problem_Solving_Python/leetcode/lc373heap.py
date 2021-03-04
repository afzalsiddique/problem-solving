import unittest
from heapq import *
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n,m = len(nums1), len(nums2)
        if m*n < k:
            return sorted([[a, b] for b in nums2 for a in nums1])
        heap = []
        for j in range(m):
            heap.append([nums1[0]+nums2[j],nums1[0],nums2[j]])
        heapify(heap)

        res = []
        i = 0
        while i!=k:
            res.append(heappop(heap)[1:3])
            i+=1
            if i<n:
                for j in range(m):
                    heappush(heap, [nums1[i]+nums2[j],nums1[i],nums2[j]])
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [[1,2],[1,4],[1,6]]
        actual = sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = [[1,1],[1,1]]
        actual = sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = [[1,3],[2,3]]
        actual = sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = [[1,3],[2,3],[1,5]]
        actual = sol.kSmallestPairs([1,2,4,5,6],[3,5,7,9],3)
        self.assertEqual(expected, actual)

