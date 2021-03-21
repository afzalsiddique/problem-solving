import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for s in strs:
            if len(s)==0:return ""
        n = len(strs)
        if n==0:return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            ch = shortest[i]
            for j in range(n):
                if ch != strs[j][i]:
                    return shortest[:i]
        return shortest

class MyTestCase(unittest.TestCase):

    def test_00(self):
        a = Solution().longestCommonPrefix([""])
        e = ""
        self.assertEqual(e,a)
    def test_0(self):
        a = Solution().longestCommonPrefix(["","",""])
        e = ""
        self.assertEqual(e,a)
    def test_01(self):
        a = Solution().longestCommonPrefix(["flower","flower","flower"])
        e = "flower"
        self.assertEqual(e,a)
    def test_1(self):
        a = Solution().longestCommonPrefix(["dog","racecar","car"])
        e = ""
        self.assertEqual(e,a)

    def test_2(self):
        a = Solution().longestCommonPrefix(["flower","flow","flight"])
        e = "fl"
        self.assertEqual(e,a)
    def test_3(self):
        a = Solution().longestCommonPrefix([])
        e = ""
        self.assertEqual(e,a)
    def test_4(self):
        a = Solution().longestCommonPrefix(['a'])
        e = "a"
        self.assertEqual(e,a)
