import string;
import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def minimumDistance(self, word: str) -> int:
        M,N=5,6
        # ANY_CHAR='#'
        def getPos(ch:str):
            i=ord(ch)-ord('A')
            return [i//N,i%N]
        def dist(ch1:str, ch2:str):
            # if ch1==ANY_CHAR or ch2==ANY_CHAR: return 0
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
        # return func(0,ANY_CHAR,ANY_CHAR) # also works

class Solution3:
    def minimumDistance(self, word: str) -> int:
        def getCord(i): return [i//6,i%6]
        def dist(i,j):
            x1,y1=getCord(i)
            x2,y2=getCord(j)
            return abs(x1-x2)+abs(y1-y2)
        @cache
        def dp(i,j,word_i): # (left finger, right finger, word index)
            if word_i==len(word):
                return 0
            minn=float('inf')
            k=word[word_i]
            minn=min(minn,dist(i,k)+dp(k,j,word_i+1)) # use left finger
            minn=min(minn,dist(j,k)+dp(i,k,word_i+1)) # use right finger
            return minn


        word=list(map(lambda x:ord(x)-ord('A'),word)) # 'CAKE' -> [2,0,10,4]
        res=float('inf')
        for i in range(26):
            for j in range(i+1,26):
                res=min(res,dp(i,j,0))

        return res
class Solution2:
    # tle. heap
    def minimumDistance(self, word: str) -> int:
        def getCord(i): return [i//6,i%6]
        def dist(i,j):
            x1,y1=getCord(i)
            x2,y2=getCord(j)
            return abs(x1-x2)+abs(y1-y2)
        word=list(map(lambda x:ord(x)-ord('A'),word))
        pq=[]
        for i in range(26):
            for j in range(i+1,26):
                heappush(pq,[0,i,j,0]) # cost,finger1,finger2,word_idx


        while pq:
            cost,i,j,word_idx=heappop(pq)
            if word_idx==len(word):
                return cost
            k=word[word_idx]
            heappush(pq,[cost+dist(i,k),k,j,word_idx+1]) # use left finger
            heappush(pq,[cost+dist(j,k),i,k,word_idx+1]) # use left finger

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
