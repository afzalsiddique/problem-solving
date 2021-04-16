import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len=float('inf')
        shortest=None
        for i in range(len(strs)):
            if len(strs[i])<shortest_len:
                shortest=strs[i]
                shortest_len=len(strs[i])
        if shortest is None: return ''
        for i in range(len(shortest)):
            c1=shortest[i]
            for j in range(len(strs)):
                c2=strs[j][i]
                if c1!=c2: return shortest[:i]
        return shortest
    def longestCommonPrefix2(self, strs: List[str]) -> str:
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

    def test0(self):
        a = Solution().longestCommonPrefix([""])
        e = ""
        self.assertEqual(e,a)
    def test1(self):
        a = Solution().longestCommonPrefix(["","",""])
        e = ""
        self.assertEqual(e,a)
    def test2(self):
        a = Solution().longestCommonPrefix(["flower","flower","flower"])
        e = "flower"
        self.assertEqual(e,a)
    def test3(self):
        a = Solution().longestCommonPrefix(["dog","racecar","car"])
        e = ""
        self.assertEqual(e,a)

    def test4(self):
        a = Solution().longestCommonPrefix(["flower","flow","flight"])
        e = "fl"
        self.assertEqual(e,a)
    def test5(self):
        a = Solution().longestCommonPrefix([])
        e = ""
        self.assertEqual(e,a)
    def test6(self):
        a = Solution().longestCommonPrefix(['a'])
        e = "a"
        self.assertEqual(e,a)
    def test7(self):
        self.assertEqual('a',Solution().longestCommonPrefix(['ab','a']))
    def test8(self):
        self.assertEqual('a',Solution().longestCommonPrefix(["abca","aba","aaab"]))
