import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect_right(letters,target)
        if idx==len(letters):
            idx = 0
        return letters[idx]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual("c", solution.nextGreatestLetter(["c", "f", "j"],"a"))

    def test_2(self):
        solution = Solution()
        self.assertEqual("f", solution.nextGreatestLetter(["c", "f", "j"],"c"))

    def test_3(self):
        solution = Solution()
        self.assertEqual("f", solution.nextGreatestLetter(["c", "f", "j"],"d"))

    def test_4(self):
        solution = Solution()
        self.assertEqual("j", solution.nextGreatestLetter(["c", "f", "j"],"g"))

    def test_5(self):
        solution = Solution()
        self.assertEqual("c", solution.nextGreatestLetter(["c", "f", "j"],"j"))

    def test_6(self):
        solution = Solution()
        self.assertEqual("c", solution.nextGreatestLetter(["c", "f", "j"],"j"))