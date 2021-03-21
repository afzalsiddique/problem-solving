import unittest




class Solution:
    def minCut(self, s: str) -> int:
        dp = {}
        def palindrome(s:str):
            return s==s[::-1]
        def helper(s:str):
            n = len(s)
            if n==0: return 0
            if n==1:return 0
            if n==2:
                if s[0]==s[1]:return 0
                else:return 1
            if s in dp:return dp[s]
            if palindrome(s):return 0
            minn = float('inf')
            for i in range(1,len(s)+1):
                first,second = s[:i], s[i:]
                if palindrome(first):
                    minn = min(minn,helper(second))
            dp[s] = 1+minn
            return dp[s]
        return helper(s)


class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().minCut('aab'))
    def test2(self):
        self.assertEqual(0, Solution().minCut('aaa'))

