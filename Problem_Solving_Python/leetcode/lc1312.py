# https://www.youtube.com/watch?v=DOnK40BvazI&t=300s
################# SAME AS LONGEST COMMON SUBSEQUENCE ##########
################ SAME AS LONGEST PALINDROMIC SUBSEQUENCE ###########
import unittest
from typing import List

class Solution:
    def minInsertions(self, s: str) -> int:
        di = {}
        def helper(s):
            n = len(s)
            if n==0 or n==1:return 0
            if n==2:
                if s[0]==s[1]:return 0
                else: return 1
            if s in di:return di[s]
            if s[0]==s[-1]:
                di[s] = helper(s[1:-1]) # remove one char from both ends
                return di[s]
            else:
                di[s]= 1+min(helper(s[:-1]), helper(s[1:]))
                return di[s]

        return helper(s)

    # longest common subsequecne
    def minInsertions2(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]
        dp = [[-1]*n for _ in range(n)]

        def helper(m,n):#longest common subsequence
            if m==-1 or n==-1:return 0
            if dp[m][n]!=-1:return dp[m][n]
            if s[m]==s2[n]:
                dp[m][n] = 1 + helper(m-1,n-1)
            else:
                dp[m][n] = max(helper(m-1,n),helper(m,n-1))
            return dp[m][n]


        return n - helper(n-1,n-1)



class MyTestCase(unittest.TestCase):

    def test_1(self):
        a =Solution().minInsertions('zzazz')
        e = 0
        self.assertEqual(e, a)


    def test_2(self):
        a =Solution().minInsertions( "mbadm" )
        e = 2
        self.assertEqual(e, a)

    def test_3(self):
        a =Solution().minInsertions( "leetcode" )
        e = 5
        self.assertEqual(e, a)
