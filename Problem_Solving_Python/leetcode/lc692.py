import unittest
from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res, heap = [],[]
        counter = Counter(words)
        i = 0
        for word in counter:
            heap.append((-counter[word], word))
        heapify(heap)
        for i in range(k):
            res.append(heappop(heap)[1])
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2)
        expected = ["i", "love"]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)
        expected = ["the", "is", "sunny", "day"]
        self.assertEqual(expected, actual)

