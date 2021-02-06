class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        m, n = len(s), len(t)
        while True:
            if i == m:
                return True
            if j == n:
                return False

            if s[i]==t[j]:
                i+= 1
                j+=1
            else:
                j+=1

