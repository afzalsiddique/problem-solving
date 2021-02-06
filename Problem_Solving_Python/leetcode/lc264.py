import unittest
from heapq import *
from typing import List


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        s = set()
        cnt = 0
        while cnt!=n:
            temp = heappop(heap)
            if temp in s:
                continue
            s.add(temp)
            heappush(heap,temp*2)
            heappush(heap,temp*3)
            heappush(heap,temp*5)
            cnt+=1
        return temp

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 12
        actual = sol.nthUglyNumber(10)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 1
        actual = sol.nthUglyNumber(1)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 2
        actual = sol.nthUglyNumber(2)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 3
        actual = sol.nthUglyNumber(3)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 4
        actual = sol.nthUglyNumber(4)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 5
        actual = sol.nthUglyNumber(5)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 6
        actual = sol.nthUglyNumber(6)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 8
        actual = sol.nthUglyNumber(7)
        self.assertEqual(expected, actual)

