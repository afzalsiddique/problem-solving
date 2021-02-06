import heapq
from collections import defaultdict
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[sum(row) for row in mat]
        n = len(arr)
        di = defaultdict(list)
        for i in range(n):
            di[arr[i]] = di[arr[i]] + [i]
        heapq.heapify(arr)

        ret = []
        for _ in range(k):
            key = heapq.heappop(arr)
            indices = di[key]
            ret.append(indices[0])
            del indices[0]
        return ret


import unittest
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual([2,0,3], solution.kWeakestRows(mat =
                                                        [[1,1,0,0,0],
                                                         [1,1,1,1,0],
                                                         [1,0,0,0,0],
                                                         [1,1,0,0,0],
                                                         [1,1,1,1,1]],
                                                        k = 3))

    def test_2(self):
        solution = Solution()
        self.assertEqual([0,2], solution.kWeakestRows(mat =
                                                            [[1,0,0,0],
                                                             [1,1,1,1],
                                                             [1,0,0,0],
                                                             [1,0,0,0]],
                                                            k = 2))