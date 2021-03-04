import unittest
from typing import List
from heapq import heappush, heappop
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans, i, N = 0, 0, len(apples)
        h = []
        while i < N or h:
            # only push to heap when you have a valid i, and the apple has atleast one day to stay fresh.
            if i<N and apples[i] > 0:
                heappush(h, [i + days[i], apples[i]])
            # remove the rotten apples batches and the batches with no apples left (which might have got consumed).
            while h and (h[0][0] <= i or h[0][1] <= 0):
                heappop(h)
            # only if there is batch in heap after removing all the rotten ones, you can eat. else wait for the subsequent days for new apple batch by incrementing i.
            if h:
                h[0][1]-=1
                ans+=1
            i+=1
        return ans 

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2])
        expected = 7
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2])
        expected = 5
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.eatenApples(0)
        expected = 0
        self.assertEqual(expected, actual)