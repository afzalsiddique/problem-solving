import unittest;


def get_sol(): return Solution()
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.longestCommonSubsequence(str1,str2)
        m,n,o=len(str1),len(str2),len(lcs)
        res=[]
        i,j,k=0,0,0
        while len(res)!=m+n-o:
            if i<m and k<o and str1[i]!=lcs[k]:
                res.append(str1[i])
                i+=1
            elif j<n and k<o and str2[j]!=lcs[k]:
                res.append(str2[j])
                j+=1
            elif i<m and j<n and k<o and str1[i]==str2[j]==lcs[k]:
                res.append(str1[i])
                i+=1
                j+=1
                k+=1
            elif i<m:
                res.append(str1[i])
                i+=1
            elif j<n:
                res.append(str2[j])
                j+=1
        return ''.join(res)

    def longestCommonSubsequence(self, a: str, b: str) -> str:
        a,b='#'+a,'#'+b
        m,n=len(a),len(b)
        dp=[[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if a[i]==b[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        res=[]
        i,j=m-1,n-1
        while i!=0 and j!=0:
            if dp[i][j]==dp[i-1][j]:
                i-=1
            elif dp[i][j]==dp[i][j-1]:
                j-=1
            else:
                res.append(a[i])
                i-=1
                j-=1
        return ''.join(res[::-1])

class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual('cabac', get_sol().shortestCommonSupersequence("abac", "cab"))
    def test_2(self):
        self.assertEqual('aaaaaaaa', get_sol().shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))
    def test_3(self):
        self.assertEqual('acbacbacaabbbb', get_sol().shortestCommonSupersequence("ababaabbbb", "cbcbacaab"))
    # def test_4(self):
