import unittest
from heapq import *
from typing import List


class Solution:
    # heap
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        s = set()
        cnt = 0
        while cnt!=n:
            temp = heappop(heap)
            if temp in s: continue
            s.add(temp)
            for prime in primes:
                heappush(heap, temp*prime)
            cnt+=1
        return temp

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 32
        actual = sol.nthSuperUglyNumber(n = 12, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 1
        actual = sol.nthSuperUglyNumber(n = 1, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 2
        actual = sol.nthSuperUglyNumber(n = 2, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 4
        actual = sol.nthSuperUglyNumber(n = 3, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 7
        actual = sol.nthSuperUglyNumber(n = 4, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 8
        actual = sol.nthSuperUglyNumber(n = 5, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 13
        actual = sol.nthSuperUglyNumber(n = 6, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 14
        actual = sol.nthSuperUglyNumber(n = 7, primes = [2,7,13,19])
        self.assertEqual(expected, actual)

