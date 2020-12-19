import unittest
from leetcode.lc126 import *


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        actual = solution.findLadders(beginWord, endWord, wordList)
        expected = [
                  ["hit","hot","dot","dog","cog"],
                  ["hit","hot","lot","log","cog"]
                ]
        self.assertEqual(expected, actual)