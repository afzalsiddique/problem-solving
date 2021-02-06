import unittest
from collections import defaultdict, Counter
from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        roots={}
        size={}
        n = len(source)

        def add(x):
            if x not in roots:
                roots[x] =x
                size[x] = 1
        def find(x):
            if x not in roots:
                p = x
            else:
                p = roots[x]
            if x==p:
                return p
            roots[x] = find(roots[x])
            return roots[x]
        def union(x,y):
            add(x),add(y)
            a, b = find(x), find(y)
            if a!=b:
                if size[a]<size[b]:
                    a,b = b, a
                roots[b] = a
                size[a]+= size[b]

        root_to_indices = defaultdict(list)
        for x,y in allowedSwaps:
            union(x,y)

        for i in range(n):
            root = find(i)
            root_to_indices[root].append(i)

        summ = 0
        for indices in root_to_indices.values():
            source_numbers = [source[idx] for idx in indices]
            target_numbers = [target[idx] for idx in indices]
            summ += sum((Counter(source_numbers) - Counter(target_numbers)).values())
        return summ

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 1
        actual = sol.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 2
        actual = sol.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = [])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.minimumHammingDistance(0)
        self.assertEqual(expected, actual)