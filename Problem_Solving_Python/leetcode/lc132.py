import unittest




class Solution:
    def minCut(self, s: str) -> int:
        di={}
        def palindrome(s):
            return True if s==s[::-1] else False
        def helper(s:str):
            if palindrome(s):return 0
            if s in di:return di[s]
            minn = float('inf')
            for i in range(1,len(s)):
                first = s[:i]
                if palindrome(first):
                    minn =min(minn,helper(s[i:]))
            di[s] = 1+minn
            return di[s]

        return helper(s)


class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().minCut('aab'))
    def test2(self):
        self.assertEqual(0, Solution().minCut('aaa'))

