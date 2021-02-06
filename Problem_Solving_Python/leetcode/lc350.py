from collections import defaultdict
from typing import List
import unittest

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        dict2 = defaultdict(int)
        for item in nums2:
            dict2[item]+=1

        for item in nums1:
            if dict2[item]>0:
                ret.append(item)
                dict2[item]-=1
        return ret




class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual([2, 2], solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

    def test_2(self):
        solution = Solution()
        self.assertEqual([4, 9], solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

    def test_3(self):
        solution = Solution()
        self.assertEqual([2], solution.intersect(nums1 = [1,2,2,1], nums2 = [2]))