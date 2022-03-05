from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem
    # https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
    def longestSubstring(self, s: str, k: int) -> int:
        count = 0
        for i in range(1, 27):
            count = max(count, self.helper(s, k, i))
        return count

    def helper(self, s, k, numUniqueTarget):
        begin = end = numUnique = count = 0
        charsAtLeastK = 0 # chars with at least k freq
        freq = defaultdict(int)

        while end < len(s):
            if freq[s[end]] == 0:
                numUnique += 1
            freq[s[end]] += 1
            if freq[s[end]] == k:
                charsAtLeastK += 1
            end += 1

            while numUnique > numUniqueTarget:
                if freq[s[begin]] == k:
                    charsAtLeastK -= 1
                freq[s[begin]] -= 1

                if freq[s[begin]] == 0:
                    numUnique -= 1
                begin += 1

            # if we found a string where the number of unique chars equals our target
            # and all those chars are repeated at least K times then update max
            if numUnique == charsAtLeastK:
            # if numUnique == numUniqueTarget and numUnique == charsAtLeastK:  # if numUnique == numUniqueTarget is redundant
                count = max(count, end-begin)

        return count
class Solution2:
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
    def test01(self):
        self.assertEqual(3, get_sol().longestSubstring('aaabb', 3))
    def test02(self):
        self.assertEqual(5, get_sol().longestSubstring('ababbc', 2))
    def test03(self):
        self.assertEqual(0, get_sol().longestSubstring('weitong', 2))
