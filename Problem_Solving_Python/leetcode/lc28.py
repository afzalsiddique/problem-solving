import unittest
from typing import List

# z algo
class Solution:
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

# KMP algo
class Solution2:
    # creating lps
    def computeLPSArray(self, pat): # geeksforgeeks
        length = 0 # length of the previous longest prefix suffix
        i = 1
        n = len(pat)
        lps=[0]*n
        while i < n:
            if pat[i]== pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1] # go back to previous longest prefix suffix
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def computeLPSArray2(self,pat:str): # abdul bari version
        pat = '#' + pat
        n = len(pat)
        i=2
        j=0
        lps=[0]*n
        while i<n:
            if pat[i]==pat[j+1]:
                lps[i]=j+1
                i+=1
                j+=1
            else:
                if j!=0:
                    j=lps[j]
                else:
                    i+=1
        return lps[1:]

    # finding pattern
    def strStr(self, haystack: str, needle: str) -> int:
        m,n= len(haystack), len(needle)
        if n==0:return 0
        if m==0:return -1
        i,j=0,0
        lps = self.computeLPSArray(needle)
        while i<m:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            if j==n:
                return i-j
            elif i<m and needle[j]!=haystack[i]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        lps = self.computeLPSArray(needle)
        n=len(haystack)
        j=0
        i=0
        while i<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==len(needle):
                    return i-j
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1
class Solution3:
    # brute force
    def strStr(self, haystack: str, needle: str) -> int:
        m,n=len(haystack),len(needle)

        if n==0:return 0
        if m==0:return -1

        for i in range(m):
            if i+n>m:break
            for j in range(n):
                if haystack[i+j]!=needle[j]:
                    break
                if j == n-1:
                    return i
        return -1



class tester(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.strStr(haystack = "hello", needle = "ll")
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.strStr(haystack = "aaaaa", needle = "bba")
        expected = -1
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.strStr(haystack = "", needle = "")
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.strStr("a","a")
        expected = 0
        self.assertEqual(expected, actual)
    def test_5(self):
        sol = Solution()
        actual = sol.strStr("mississippi","mississippi")
        expected = 0
        self.assertEqual(expected, actual)
    def test_6(self):
        sol = Solution()
        actual = sol.strStr( "mississippi" ,"issipi")
        expected = -1
        self.assertEqual(expected, actual)
    def test_7(self):
        sol = Solution()
        actual = sol.strStr( "mississippi" ,"issip")
        expected = 4
        self.assertEqual(expected, actual)
