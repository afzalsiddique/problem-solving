import string;
import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def minimumDistance(self, word: str) -> int:
        M,N=5,6
        # START='#'
        def getPos(ch:str):
            i=ord(ch)-ord('A')
            return [i//N,i%N]
        def dist(ch1:str, ch2:str):
            # if ch1==START or ch2==START: return 0
            i1,j1=getPos(ch1)
            i2,j2=getPos(ch2)
            return abs(i1-i2) + abs(j2-j1)
        @functools.lru_cache(None)
        def func(i:int,ch1:str,ch2:str):
            if i==n: return 0
            return min(dist(ch1,word[i])+func(i+1,word[i],ch2),
                       dist(ch2,word[i])+func(i+1,ch1,word[i]))

        n=len(word)
        res=float('inf')
        for x in string.ascii_uppercase:
            for y in string.ascii_uppercase:
                res=min(res,func(0,x,y))
        return res
        # return func(0,START,START) # also works


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minimumDistance(word = "CAKE"))
    def test2(self):
        self.assertEqual(6, get_sol().minimumDistance(word = "HAPPY"))
    def test3(self):
        self.assertEqual(3, get_sol().minimumDistance(word = "NEW"))
    def test4(self):
        self.assertEqual(7, get_sol().minimumDistance(word = "YEAR"))
    def test5(self):
        self.assertEqual(500, get_sol().minimumDistance(word = "KXGJRDQYJCDRTJXBHDVFOFFOIWFOWSARMADDJCUYMGIXMHOUTQRLFNUZASNTHJLQKPUYXOXWILIYFFHOKUALPTZWJVHADOXQFGMWTKREBPNOZOLAGSGCPEVCXQWVRMTIGCNARPWXKXAGTJYYZNOWQWJCBCLMUNMZUWYUYHJPMRAUNUJVPEMVNMWYSXTJPRLJNSUYFLBNOOJCVHKHMATKEFPCYDFTBHUFAUQVNVNFJMOJRBFPFDVDPXJXZJJMBSIK"))
