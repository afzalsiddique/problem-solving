import unittest
from collections import Counter
from heapq import *
from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        di = dict(Counter(s))
        heap = [(-di[letter], letter) for letter in di]
        heapify(heap)
        res = []
        while heap:
            value, letter = heappop(heap)
            res.append(letter*(-value))
        return "".join(res)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.frequencySort("tree")
        expected = "eert"
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.frequencySort("cccaaa")
        expected = "aaaccc"
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.frequencySort("Aabb")
        expected = "bbAa"
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.frequencySort(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.frequencySort(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.frequencySort(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.frequencySort(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.frequencySort(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.frequencySort(0)
        self.assertEqual(expected, actual)