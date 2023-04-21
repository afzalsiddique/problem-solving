from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution3()

# interesting property of Counter
# Counter({'a':2,'b':1}) - Counter({'a':1,'b':2}) = Counter({'a':1})

class Solution3:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def serialize(count:Counter): # serialize a Counter. Counter('a':1,'c':2) -> (1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            return tuple(count[ch] for ch in string.ascii_lowercase)
        def deserialize(tup:tuple): # deserialize the Counter. (1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) -> Counter('a':1,'c':2)
            return Counter({ch:val for ch,val in zip(string.ascii_lowercase,tup)})
        @cache
        def dfs(i, hashed: tuple):
            count=deserialize(hashed)

            if all(count[c]==0 for c in count): return 0 # option1
            # if i==len(target): return 0 # option 2

            char=target[i]
            res=float('inf')
            if count[char]==0:
                return dfs(i + 1, serialize(count))
            for j in range(n):
                if char in freqs[j]:
                    res=min(res, 1 + dfs(i, serialize(count - freqs[j])))
            return res

        n=len(stickers)
        freqs=[Counter(s) for s in stickers]
        res= dfs(0, serialize(Counter(target)))
        return res if res!=float('inf') else -1
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def serialize(count:Counter): # serialize a Counter. Counter('a':1,'c':2) -> (1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            return tuple(count[ch] for ch in string.ascii_lowercase)
        def deserialize(tup:tuple): # deserialize the Counter. (1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) -> Counter('a':1,'c':2)
            return Counter({ch:val for ch,val in zip(string.ascii_lowercase,tup)})
        @cache
        def dp(ch_i:int,tup:tuple):
            count=deserialize(tup)
            if ch_i==26: return 0
            ch=chr(ord('a')+ch_i)

            # if ch_i th char is not required then move to the next char. Example: if 'a' is not required move to 'b'
            if count[ch]==0: return dp(ch_i+1,tup)
            res=float('inf')
            for i in range(n):
                if myStickers[i][ch]==0: continue # stickers[i] does not contain ch_i th char. Example: "with" does not 0 th char (0 th char is 'a')
                newCount=count-myStickers[i]
                res=min(res,1+dp(ch_i,serialize(newCount)))
            return res

        n=len(stickers)
        myStickers = [Counter(s) for s in stickers]
        ans=dp(0,serialize(Counter(target)))
        return ans if ans!=float('inf') else -1
class Solution5:
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
        @cache
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

class Solution4:
    # tle
    def minStickers(self, stickers: List[str], target: str) -> int:
        def counter_to_hashable(count:Counter):
            return tuple(count[ch] for ch in string.ascii_lowercase)
        def hashable_to_counter(tup:tuple):
            return Counter({ch:val for ch,val in zip(string.ascii_lowercase,tup)})
        def hasEveryLetter(count:Counter):
            return all(count[ch]<=0 for ch in count)
        def everyLetterFromIthStickerAlreadyTaken(i,count):
            letters=set(stickers[i])
            return all(count[ch]<=0 for ch in letters)
        @cache
        def dfs(i,tup):
            count=hashable_to_counter(tup)
            if hasEveryLetter(count):
                return 0
            res=float('inf')
            for j in range(i,len(stickers)):
                if everyLetterFromIthStickerAlreadyTaken(j,count): continue
                hashable_counter=counter_to_hashable(count-Counter(stickers[j]))
                tmp=dfs(j,hashable_counter)
                res=min(res,tmp)
            return res+1


        ans=dfs(0,counter_to_hashable(Counter(target)))
        return ans if ans!=float('inf') else -1
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
    def test6(self):
        self.assertEqual(4,get_sol().minStickers(["heart","seven","consider","just","less","back","an","four","cost","kill","skin","happen","depend","broad","caught","fast","fig","way","under","print","white","war","sent","locate","be","noise","door","get","burn","quite","eight","press","eye","wave","bread","wont","short","cow","plain","who","well","drive","fact","chief","store","night","operate","page","south","once"], "chargeresult"))
    # def test7(self):
    # def test8(self):
