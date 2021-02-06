# https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root=list(range(n))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x,y):
            root[find(x)] = root[find(y)]

        for x,y in pairs:
            union(x,y)

        di = defaultdict(list)
        for i in range(n):
            di[find(i)].append(s[i])

        for comp_id in di:
            di[comp_id].sort(reverse=True)

        res = []
        for i in range(n):
            res.append(di[find(i)].pop())
        return ''.join(res)




class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = "bacd"
        actual = sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = "abcd"
        actual = sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = "abc"
        actual = sol.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]])
        self.assertEqual(expected, actual)

