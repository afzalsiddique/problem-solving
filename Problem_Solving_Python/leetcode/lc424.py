import unittest
from collections import defaultdict
from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = defaultdict(int)
        start,maxx = 0,0
        for end in range(n):
            count[s[end]]+=1
            most_freq_letter_cnt = max(count.values())
            letters_to_change = end-start+1-most_freq_letter_cnt
            if letters_to_change>k:
                count[s[start]]-=1
                start+=1
            maxx = max(maxx, end-start+1)
        return maxx

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "ABAB", k = 2)
        expected = 4
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "AABABBA", k = 1)
        expected = 4
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "AAAAA", k = 1)
        expected = 5
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "AAAAAB", k = 1)
        expected = 6
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "BAAAAA", k = 1)
        expected = 6
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "AABB", k = 3)
        expected = 4
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "ABCABCAB", k = 3)
        expected = 5
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "ABCABCAB", k = 2)
        expected = 4
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.characterReplacement(s = "ABCDABCDAB", k = 3)
        expected = 5
        self.assertEqual(expected, actual)