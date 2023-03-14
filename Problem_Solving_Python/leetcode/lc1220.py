import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD=10**9+7
        ANY='#'
        canFollow = {'a':['e',ANY],'e':['a','i',ANY],'i':['a','e','o','u',ANY],'o':['i','u',ANY],'u':['a',ANY]}
        @functools.lru_cache(None)
        def dp(n:int,last:str):
            if n==0:
                return 1
            res=0
            for ch in ['a','e','i','o','u']:
                if last in canFollow[ch]:
                    res+=dp(n-1,ch)
                    res%=MOD
            return res

        return dp(n,ANY)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, get_sol().countVowelPermutation(1))
    def test2(self):
        self.assertEqual(10, get_sol().countVowelPermutation(2))
    def test3(self):
        self.assertEqual(68, get_sol().countVowelPermutation(5))
    def test4(self):
        self.assertEqual(18208803, get_sol().countVowelPermutation(144))
    # def test5(self):
    # def test6(self):
    # def test7(self):

