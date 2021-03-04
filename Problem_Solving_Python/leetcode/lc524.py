import unittest
from typing import List
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99583/Python-Simple-(Two-pointer)
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/1077674/Python-O(mn)-solution-explained
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x:(-len(x),x))
        for word in d:
            if self.is_substring(s, word):
                return word
        return ""
    def is_substring(self, s, word):
        j=0
        for i in range(len(s)):
            if word[j]==s[i]:
                j+=1
            if j==len(word):
                return True
        return False


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"])
        expected = "apple"
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.findLongestWord(s = "abpcplea", d = ["a","b","c"])
        expected = "a"
        self.assertEqual(expected, actual)

