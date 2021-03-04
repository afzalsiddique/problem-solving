# https://leetcode.com/problems/largest-merge-of-two-strings/discuss/1053513/Python-greedy
import unittest
from typing import List


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        if word1>word2:
            return word1[0] + self.largestMerge(word1[1:], word2)
        else:
            return word2[0] + self.largestMerge(word1, word2[1:])




class MyTestCase(unittest.TestCase):

    def test_1234(self):
        sol = Solution()
        actual = sol.largestMerge(word1="aa", word2="aa")
        expected = "aaaa"
        self.assertEqual(expected, actual)

    def test_1(self):
        sol = Solution()
        actual = sol.largestMerge(word1="cabaa", word2="bcaaa")
        expected = "cbcabaaaaa"
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.largestMerge(word1="abcabc", word2="abdcaba")
        expected = "abdcabcabcaba"
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.largestMerge(word1="abc", word2="abc")
        expected = "abcabc"
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.largestMerge(word1="a", word2="a")
        expected = "aa"
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.largestMerge(word1="ba", word2="a")
        expected = "baa"
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.largestMerge(word1="qabc", word2="wabc")
        expected = "wqabcabc"
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.largestMerge(word1="aaaz", word2="aaab")
        expected = "aaazaaab"
        self.assertEqual(expected, actual)

    # def test_8(self):
    #     sol = Solution()
    #     actual = sol.largestMerge("guguuguguuuguug", "gguggguuggguugg")
    #     expected = "guguuguguuuguugguggguuggguuggg"
    #     self.assertEqual(expected, actual)
    #
    # def test_9(self):
    #     sol = Solution()
    #     actual = sol.largestMerge("guguuguguuguug", "ggugguugguugg")
    #     expected = "guguuguguuguuggugguugguuggg"
    #     self.assertEqual(expected, actual)
    #
    # def test_10(self):
    #     sol = Solution()
    #     actual = sol.largestMerge("guguuguug", "gguugguugg")
    #     expected = "guguuguugguugguuggg"
    #     self.assertEqual(expected, actual)
    #
    # def test_11(self):
    #     sol = Solution()
    #     actual = sol.largestMerge("guuguug", "gguugg")
    #     expected = "guuguugguuggg"
    #     self.assertEqual(expected, actual)

    def test_12(self):
        sol = Solution()
        actual = sol.largestMerge("gug", "ggu")
        expected = "guggug"
        self.assertEqual(expected, actual)