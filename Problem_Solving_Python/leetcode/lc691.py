import string;
from collections import Counter;
import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/stickers-to-spell-word/discuss/161470/My-Python-DFS-Solution/333443
    def minStickers(self, stickers, target):
        def func(s): return Counter(c for c in s if c in target)
        def dfs(cur_cnt, used, i):
            char=target[i] if i<n else ''
            nonlocal res
            if i == n:
                res = used
            elif cur_cnt[char] >= target_cnt[char]:
                dfs(cur_cnt, used, i + 1)
            elif used + 1 < res:
                for sticker in freqs:
                    if target[i] in sticker:
                        dfs(cur_cnt + sticker, used + 1, i + 1)

        target_cnt, res, n = Counter(target), float("inf"), len(target)
        freqs=[func(s) for s in stickers]
        dfs(Counter(), 0, 0)
        return res if res < float("inf") else -1
class Solution3:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def func(s): return Counter(c for c in s if c in target)
        def serialize(count:Counter): # serialize a Counter. Counter('a':1,'c':2) -> "1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
            li = [str(count[c]) for c in string.ascii_lowercase]
            return ','.join(li)
        def deserialize(hashed:str): # deserialize the Counter. "1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0" -> Counter('a':1,'c':2)
            li = hashed.split(',')
            count = Counter()
            for c in string.ascii_lowercase:
                idx = ord(c)-ord('a')
                if int(li[idx]):
                    count[c]=int(li[idx])
            return count
        @functools.lru_cache(None)
        def dfs(hashed:str,i):
            count=deserialize(hashed)
            if all(count[c]==0 for c in count):
                return 0
            char=target[i]
            res=float('inf')
            if count[char]==0:
                res=min(res,dfs(serialize(count),i+1))
            else:
                for j in range(n):
                    if char in freqs[j]:
                        res=min(res,1+dfs(serialize(count-freqs[j]),i))
            return res

        n=len(stickers)
        freqs=[func(s) for s in stickers]
        res=dfs(serialize(Counter(target)),0)
        return res if res!=float('inf') else -1
class Solution2:
    # tle
    def minStickers(self, stickers: List[str], target: str) -> int:
        def func(s): return Counter(c for c in s if c in target)
        def subtract_available(c1,c2):
            for c in c2:
                if c in c1: return True
            return False
        def serialize(count:Counter): # serialize a Counter. Counter('a':1,'c':2) -> "1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
            li = [str(count[c]) for c in string.ascii_lowercase]
            return ','.join(li)
        def deserialize(hashed:str): # deserialize the Counter. "1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0" -> Counter('a':1,'c':2)
            li = hashed.split(',')
            count = Counter()
            for c in string.ascii_lowercase:
                idx = ord(c)-ord('a')
                if int(li[idx]):
                    count[c]=int(li[idx])
            return count
        @functools.lru_cache(None)
        def dfs(i,hashed:str):
            count=deserialize(hashed)
            if all(count[c]==0 for c in count): return 0
            res=float('inf')
            for j in range(i,n):
                if subtract_available(count,freqs[j]):
                    res=min(res,1+dfs(j,serialize(count-freqs[j])))
            return res

        n=len(stickers)
        freqs=[func(s) for s in stickers]
        res= dfs(0,serialize(Counter(target)))
        return res if res!=float('inf') else -1

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,get_sol().minStickers(stickers = ["with","example","science"], target = "thehat"))
    def test2(self):
        self.assertEqual(-1,get_sol().minStickers(stickers = ["notice","possible"], target = "basicbasic"))
    def test3(self):
        self.assertEqual(3,get_sol().minStickers(["these","guess","about","garden","him"], "atomher"))
    def test4(self):
        self.assertEqual(3,get_sol().minStickers(["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"], "stoodcrease"))
    def test5(self):
        self.assertEqual(3,get_sol().minStickers(["point","square","love","show","ran","certain","soil","period","say","human","duck","meet","speed","lie","differ","depend","thank","floor","sail","father","spring","field","music","too","interest","suit","new","finish","electric","parent","song","read","who","effect","fall","spoke","on","short","center","organ","plain","straight","near","so","she","science","quick","position","problem","history"], "chargeresult"))
    # def test6(self):
    # def test7(self):
    # def test8(self):
