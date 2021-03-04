import unittest
from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = [(nums[i], i) for i in range(len(nums)-k+1)]
        heapify(pq)
        res = []
        last_idx = -1
        while k!=0:
            num, i = heappop(pq)
            if i>last_idx:
                k-=1
                heappush(pq, (nums[-k], n-k))
                res.append(num)
                last_idx = i
        return res
class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.mostCompetitive(nums = [3,5,2,6], k = 2)
        expected = [2,6]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4)
        expected = [2,3,3,4]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], k=3)
        expected = [8,80,2]
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.mostCompetitive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.mostCompetitive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.mostCompetitive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.mostCompetitive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.mostCompetitive(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.mostCompetitive(0)
        expected = 0
        self.assertEqual(expected, actual)