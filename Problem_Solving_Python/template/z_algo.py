# https://www.youtube.com/watch?v=CpZh4eF8QBw
class Solution:
    # leetcode 28
    def strStr(self, haystack: str, needle: str) -> int:
        def get_z_values(s):
            n, l, r = len(s), 0, 0
            z = [0 for _ in range(n)]
            for i in range(1, n):
                if i > r:
                    l, r = i, i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
                else:
                    if z[i - l] + i - 1 < r:
                        z[i] = z[i - l]
                    else:
                        l = i
                        while r < n and s[r - l] == s[r]:
                            r += 1
                        z[i] = r - l
                        r -= 1
            return z

        m,n = len(needle), len(haystack)
        if m==0:return 0
        z = get_z_values(needle+"$"+haystack)
        for i in range(m+1, n+m+1):
            if z[i] == m:
                return i- m-1
        return -1
