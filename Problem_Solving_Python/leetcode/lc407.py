# https://www.youtube.com/watch?v=m18Hntz4go8
# https://www.youtube.com/watch?v=cJayBq38VYw
import unittest
from heapq import *
from typing import List


class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        n, m = len(height), len(height[0])
        pq = []
        vis = [[False] * m for _ in range(n)]
        for i in range(n): # all points at the edge
            for j in range(m):
                if i == 0 or i == n - 1:
                    pq.append((height[i][j], i, j))
                else:
                    if j == 0 or j == m - 1:
                        pq.append((height[i][j], i, j))

        heapify(pq)
        maxx = 0
        ans = [[0] * m for _ in range(n)]
        while pq:
            h, i, j = heappop(pq)
            vis[i][j]=True
            if h >= maxx:
                maxx = h
            else:
                ans[i][j] = maxx - h
            if i + 1 < n and vis[i + 1][j] == False:
                heappush(pq, (height[i + 1][j], i + 1, j))
                vis[i + 1][j] = True
            if j + 1 < m and vis[i][j + 1] == False:
                heappush(pq, (height[i][j + 1], i, j + 1))
                vis[i][j + 1] = True
            if i - 1 >= 0 and vis[i - 1][j] == False:
                heappush(pq, (height[i - 1][j], i - 1, j))
                vis[i - 1][j] = False
            if j - 1 >= 0 and vis[i][j - 1] == False:
                heappush(pq, (height[i][j - 1], i, j - 1))
                vis[i][j - 1] = False
        # for x in ans:
        #     print(x)
        return sum([sum(row) for row in ans])


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.trapRainWater([
            [1, 4, 3, 1, 3, 2],
            [3, 2, 1, 3, 2, 4],
            [2, 3, 3, 2, 3, 1]
        ])
        expected = 4
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.trapRainWater([[12, 13, 1, 12],
                                    [13, 4, 13, 12],
                                    [13, 8, 10, 12],
                                    [12, 13, 12, 12],
                                    [13, 13, 13, 13]])
        expected = 14
        self.assertEqual(expected, actual)

