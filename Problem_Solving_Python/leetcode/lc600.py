import unittest;


def get_sol(): return Solution()
class Solution:
    def findIntegers(self, num):
        s = bin(num + 1)[2:]
        n = len(s)
        dp = [1, 2] + [0]*(n-2)
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        flag, ans = 0, 0
        for i in range(n):
            if s[i] == "0": continue
            if flag == 1: break
            if i > 0 and s[i-1] == "1": flag = 1
            ans += dp[-i-1]

        return ans


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, get_sol().findIntegers(5))
    def test2(self):
        self.assertEqual(2, get_sol().findIntegers(1))
    def test3(self):
        self.assertEqual(3, get_sol().findIntegers(3))
    def test4(self):
        self.assertEqual(6, get_sol().findIntegers(8))
    def test5(self):
        self.assertEqual(10, get_sol().findIntegers(17))
    def test6(self):
        self.assertEqual(34, get_sol().findIntegers(100))
    # def test7(self):
    # def test8(self):
