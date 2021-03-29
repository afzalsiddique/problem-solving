import unittest
from collections import Counter


class Solution:
    # https://www.youtube.com/watch?v=bHZkCAcj3dc
    def longestSubstring(self, s: str, k: int) -> int:
        problematic_letters = []
        valid = True
        counter = Counter(s)
        for letter in counter:
            if counter[letter] < k:
                problematic_letters.append(letter)
                valid = False
        if valid:
            return len(s)

        for letter in problematic_letters:
            s = s.replace(letter, ' ')
        strings_after_divide = s.split()

        ans = 0
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans

class MyTestCase(unittest.TestCase):
    def test_8(self):
        solution = Solution()
        s = 'aaabb'
        k = 3
        actual = solution.longestSubstring(s, k)
        expected = 3
        self.assertEqual(expected, actual)

    def test_9(self):
        solution = Solution()
        s = 'ababbc'
        k = 2
        actual = solution.longestSubstring(s, k)
        expected = 5
        self.assertEqual(expected, actual)

    def test_10(self):
        solution = Solution()
        s = 'weitong'
        k = 2
        actual = solution.longestSubstring(s, k)
        expected = 0
        self.assertEqual(expected, actual)
