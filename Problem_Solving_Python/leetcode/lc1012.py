import unittest;


def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=rGGo4FA7CeU
    # leetcode 902
    # find numbers with no duplicate digits
    # return n - find numbers with no duplicate digits
    def numDupDigitsAtMostN(self, n: int) -> int:
        target=[int(x) for x in str(n)]
        def f(n): # factorial
            if n == 0 or n == 1: return 1
            return f(n-1) * n
        def nPr(n, r): # permutation. choose r out of n items
            return f(n) // f(n - r)

        n_num=len(str(n))
        if n_num==1: return n-min(9,n)

        res=0 # without repeated digits

        # for i in range(n_num-1): # also works
        #     cur=1
        #     cur*=9
        #     for j in range(i):
        #         cur*=10-(j+1)
        #     res+=cur

        # less digits
        for i in range(n_num-1): # i=0->9; i=1->9*9; i=2->9*9*8; i=3->9*9*8*7; i=4->9*9*8*7*6
            cur=9
            cur*=nPr(9,i)
            res+=cur

        # equal digits
        for i in range(n_num):
            hope_to_find_same_number=False
            for d in range(10):
                if i==0 and d==0: # no leading zeros
                    continue
                if d in target[:i]: # d already used
                    continue
                if d>target[i]:
                    break
                if d==target[i]:
                    hope_to_find_same_number=True
                    break
                res+=nPr(10 - (i + 1), n_num - (i + 1))
            if not hope_to_find_same_number:
                return n-res

        return n-(res+hope_to_find_same_number)
        # return n-(res+(len(target)==len(set(target))))
class Solution2:
    # tle
    def numDupDigitsAtMostN(self, n: int) -> int:
        def dfs(s:str):
            nonlocal res
            if len(set(s))!=len(s):
                return
            if int(s)>n or int(s)<1:
                return
            res+=1
            for i in range(9+1):
                dfs(s+str(i))


        res=0
        for i in range(1,9+1):
            dfs(str(i))
        return n-res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().numDupDigitsAtMostN(20))
    def test02(self):
        self.assertEqual(10,get_sol().numDupDigitsAtMostN(100))
    def test03(self):
        self.assertEqual(262,get_sol().numDupDigitsAtMostN(1000))
    def test04(self):
        self.assertEqual(612924,get_sol().numDupDigitsAtMostN(743610))
    def test05(self):
        self.assertEqual(994388230,get_sol().numDupDigitsAtMostN(1000000000))
    def test06(self):
        self.assertEqual(0,get_sol().numDupDigitsAtMostN(1))
    def test07(self):
        self.assertEqual(1,get_sol().numDupDigitsAtMostN(12))
    # def test08(self):
    # def test09(self):
