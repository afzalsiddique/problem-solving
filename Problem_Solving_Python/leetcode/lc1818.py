from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    ## TLE
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        abs_values = []
        n = len(nums1)
        for n1,n2 in zip(nums1,nums2):
            abs_values.append(abs(n1-n2))
        total = sum(abs_values)
        minn = total
        for i in range(n):
            for j in range(n):
                nums1[i],nums1[j]=nums1[j],nums1[i]
                tmp = abs(nums1[i]-nums2[i])
                if tmp<abs_values[i]:
                    diff = abs(tmp-abs_values[i])
                    minn = min(minn, total-diff)
                nums1[i],nums1[j]=nums1[j],nums1[i]
        return minn

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(20,Solution().minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]))
#     def test2(self):
#         self.assertEqual([1,1,0,0],Solution().findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))