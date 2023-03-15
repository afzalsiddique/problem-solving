import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def strangePrinter(self, s: str) -> int:
        @functools.lru_cache(None)
        def func(i,j,k):
            if i>j: return 0
            if i==j: return 1
            res=float('inf')
            if s[i]==s[i+1]:
                res=min(res,1+func(i+1,j,k+1))
            for m in range(i+1,j+1):
                if s[i]==s[m]:
                    part1=func(i+1,m-1,0)
                    part2=func(m,j,k+1)
                    res=min(res,part1+part2)
                else:
                    part1=1
                    part2=func(i+1,j,0)
                    res=min(res,part1+part2)
            return res

        return func(0,len(s)-1,0)



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().strangePrinter("abbb"))
    def test02(self):
        self.assertEqual(2, get_sol().strangePrinter("aaabbb"))
    def test03(self):
        self.assertEqual(2, get_sol().strangePrinter("aba"))
    def test04(self):
        self.assertEqual(1, get_sol().strangePrinter("bb"))
    def test05(self):
        self.assertEqual(1, get_sol().strangePrinter("bbb"))
    def test06(self):
        self.assertEqual(1, get_sol().strangePrinter("bbb"))
    def test07(self):
        self.assertEqual(14, get_sol().strangePrinter("abcdefghijklmn"))
    def test08(self):
        self.assertEqual(3, get_sol().strangePrinter("abbc"))
    def test09(self):
        self.assertEqual(7, get_sol().strangePrinter("abcabcabc"))
    def test10(self):
        self.assertEqual(5, get_sol().strangePrinter("abcabc"))
