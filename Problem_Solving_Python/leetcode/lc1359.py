import unittest;


def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=H0Yl1AlUuK8&t=243s
    def countOrders(self, n: int) -> int:
        MOD=10**9+7
        res=1
        for i in range(1,n+1):
            res*=i
            res%=MOD
            res*=(2*i-1)
            res%=MOD
        return res
class Solution2:
    # Assume we have already n - 1 pairs, now we need to insert the nth pair.
    # To insert the first element, there are n * 2 - 1 choices of position。
    # To insert the second element, there are n * 2 choices of position。
    # So there are (n * 2 - 1) * n * 2 permutations.
    # Considering that delivery(i) is always after of pickup(i), we need to divide 2.
    # So it's (n * 2 - 1) * n
    def countOrders(self, n: int) -> int:
        res=1
        for i in range(2,n+1):
            res*=(i*2-1)*(i*2)//2
            res%=10**9+7
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().countOrders(1))
    def test02(self):
        self.assertEqual(6,get_sol().countOrders(2))
    def test03(self):
        self.assertEqual(90,get_sol().countOrders(3))
    def test04(self):
        self.assertEqual(729647433,get_sol().countOrders(8))
    # def test05(self):
    # def test06(self):
