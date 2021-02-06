import unittest
from bisect import bisect_left


class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins_left = n
        li = [1]
        coins_left -= 1

        i = 2
        while coins_left > 0:
            li.append(li[-1] + i)
            coins_left -= i
            i += 1
        idx = bisect_left(li, n)
        if li[idx] == n:
            return idx + 1
        return idx


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(2, sol.arrangeCoins(5))

    def test_2(self):
        sol = Solution()
        self.assertEqual(3, sol.arrangeCoins(8))

    def test_3(self):
        sol = Solution()
        self.assertEqual(1, sol.arrangeCoins(1))

    def test_4(self):
        sol = Solution()
        self.assertEqual(1, sol.arrangeCoins(2))

    def test_5(self):
        sol = Solution()
        self.assertEqual(2, sol.arrangeCoins(3))
