import unittest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s)->int:
        start = maxLength = 0
        usedChar = {} # (key,value) = (char, index)

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # In the example, "abcdefb" when right pointer is at 2nd 'b',
                # the left pointer will move to 'c'
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


    def lengthOfLongestSubstring_(self, s: str) -> int:
        n = len(s)
        sett = set()
        l, r = 0, 0
        while r<n:
            if s[r] in sett:
                break
            sett.add(s[r])
            r += 1
        maxx = r
        while r < n:
            if s[r] in sett:
                sett.remove(s[l])
                l += 1
            else:
                sett.add(s[r])
                r += 1
            maxx = max(maxx, r - l)
        return maxx



class MyTestClass(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = 'abcabcbb'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = 'bbbbbbb'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 1
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = 'pwwkew'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = ''
        actual = solution.lengthOfLongestSubstring(s)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        s = 'b'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 1
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        s = 'abc'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        s = 'abcabc'
        actual = solution.lengthOfLongestSubstring(s)
        expected = 3
        self.assertEqual(expected, actual)

    def test_8(self):
        solution = Solution()
        s = ' '
        actual = solution.lengthOfLongestSubstring(s)
        expected = 1
        self.assertEqual(expected, actual)
