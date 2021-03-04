import unittest
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def check_left(x, di):
            if x not in di:return 0
            prev = x-1
            if prev not in di:
                return di[x]
            if di[prev]==0:
                return di[x]
            ret = check_left(prev, di)
            di[x] = di[x] + ret
            di[prev] = 0
            return di[x]
        di={x:1 for x in nums}
        if len(nums)==0:return 0
        for x in di:
            check_left(x, di)
        return max(di.values())


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.longestConsecutive([3,1,4,2])
        expected = 4
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.longestConsecutive( nums = [0,3,7,2,5,8,4,6,0,1])
        expected = 9
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.longestConsecutive(0)
        expected = 0
        self.assertEqual(expected, actual)