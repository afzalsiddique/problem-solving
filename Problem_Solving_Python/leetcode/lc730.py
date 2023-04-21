import unittest;


def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=x3OxiEc523Y
    # https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109507/Java-96ms-DP-Solution-with-Detailed-Explanation
    def countPalindromicSubsequences(self, s: str) -> int:
        n=len(s)
        MOD=10**9+7
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                    continue
                if j-i+1==2:
                    dp[i][j]=2
                    continue
                if s[i]==s[j]:
                    lo=i+1
                    hi=j-1
                    while lo<=hi and s[lo]!=s[i]:
                        lo+=1
                    while lo<=hi and s[hi]!=s[j]:
                        hi-=1
                    if lo>hi:
                         # consider the string from i to j is "a...a" "a...a"... where there is no character 'a' inside the leftmost and rightmost 'a'
                         # eg 'aba'
                         # inner palindromes are: ['b']
                         # add 'a' to both sides of the inner palindrome: ['aba']. That's why '*2'
                         # Then there are also: ['a','aa']. So add 2.
                        dp[i][j]=dp[i+1][j-1]*2+2
                    elif lo==hi:
                        # consider the string from i to j is "a...a...a" where there is only one character 'a' inside the leftmost and rightmost 'a'
                        # eg 'aaa'
                        # inner palindromes are: ['a']
                        # add 'a' to both sides of the inner palindrome: ['aaa']. That's why '*2'
                        # Then there is also ['aa']. So add 1.
                        dp[i][j]=dp[i+1][j-1]*2+1
                    else:
                        # consider the string from i to j is "a...a...a... a" where there are at least two character 'a' close to leftmost and rightmost 'a'
                        # eg: "aacaa"
                        # inner palindromes are: ['a','c','aca']
                        # add 'a' to both sides of the inner palindrome: ['aaa','aca','aacaa']. That's why '*2'
                        # then subtract the inner palindromes which were already counted previously
                        dp[i][j]=dp[i+1][j-1]*2-dp[lo+1][hi-1]
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                dp[i][j]%=MOD
        return dp[0][-1]
class Solution2:
    # recursion though very similar to bottom-up
    # https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/754057/Evolve-from-recursion-to-dp
    def countPalindromicSubsequences(self, s: str) -> int:
        return 0


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6,get_sol().countPalindromicSubsequences('bccb'))
    def test_2(self):
        self.assertEqual(104860361,get_sol().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
