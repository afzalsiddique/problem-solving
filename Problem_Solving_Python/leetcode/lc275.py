import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left,right = 0,n-1
        while left<=right:
            mid=(left+right)//2
            cnt=n-mid
            if citations[mid]==cnt: # even if we have duplicates it works. eg 1,2,3,3,3,3,3,4,5
                return cnt
            if citations[mid]<cnt:
                left=mid+1
            else:
                right=mid-1
        return n-left # After iteration, it is guaranteed that left is the one we need to find (i.e. len-left papars have at least len-left citations)

class MyTestCase(unittest.TestCase):
    def test_explain1(self):
        self.assertEqual(3,Solution().hIndex([0,1,2,3,7,8]))
    def test_explain2(self):
        self.assertEqual(4,Solution().hIndex([1,5,6,7,8]))
    def test_explain3(self):
        self.assertEqual(4,Solution().hIndex([1,4,6,7,8]))
    def test_explain4(self):
        self.assertEqual(3,Solution().hIndex([1,3,6,7,8]))
    def test_1(self):
        sol = Solution()
        expected = 3
        actual = sol.hIndex(citations = [0,1,3,5,6])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 7
        actual = sol.hIndex([2,7,10,12,13,14,15,16])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 7
        actual = sol.hIndex([2,8,11,12,13,14,15,16])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 3
        actual = sol.hIndex([4,6,9])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 1
        actual = sol.hIndex([1,3])
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.hIndex([])
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 3
        actual = sol.hIndex([1,2,3,3,3,3,3,4,5])
        self.assertEqual(expected, actual)
