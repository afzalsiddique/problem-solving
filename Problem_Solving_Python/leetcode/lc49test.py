import unittest
from leetcode.lc49 import *
class MyTestCase(unittest.TestCase):

    # def test_1(self):
    #     solution = Solution()
    #     strs = ["eat","tea","tan","ate","nat","bat"]
    #     actual = solution.groupAnagrams(strs)
    #     actual = sorted(actual)
    #     expected = sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
    #     self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        strs = [""]
        actual = solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        strs = ["a"]
        actual = solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(expected, actual)