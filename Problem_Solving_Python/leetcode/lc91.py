class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(s, p):
            n = len(s)
            if p==n:
                return 1
            if s[p] == '0':
                return 0
            first = int(s[p])
            firstTwo = int(s[p:p+2])
            ans = 0
            if first != 0:
                ans += helper(s, p+1)
            if p + 1 < n and 0 < firstTwo < 27:
                ans += helper(s, p+2)
            return ans
        return helper(s, 0)