from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://miro.medium.com/max/3000/1*MvTnZScOoc6P1ZQR7lzOHg.png
    # https://medium.com/@jolyon129/854-k-similar-strings-7b68772217d0
    def kSimilarity(self, s1: str, s2: str) -> int:
        q=deque()
        n=len(s1)
        s1=list(s1)
        q.append((s1,0))
        res=0
        while q:
            for _ in range(len(q)):
                s1,i=q.popleft()
                j=i
                while i<n and s1[i]==s2[j]:
                    i+=1
                    j+=1
                if i==n: return res
                while i<n:
                    if s1[i]==s2[i]:
                        i+=1
                        continue
                    if s1[i]==s2[j]:
                        tmp=s1[:]
                        tmp[i],tmp[j]=tmp[j],tmp[i]
                        q.append((tmp,j))
                    i+=1
            res+=1

class Solution2:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def removeSameChars(l1:List[str], l2:List[str]): # ('abdc','abcd') -> ('dc','cd')
            indices = [i for i in range(len(l1)) if l1[i] != l2[i]]
            l1 = [l1[i] for i in indices]
            l2 = [l2[i] for i in indices]
            return [l1, l2]
        @cache
        def swapFirstCharOfS1(s1:str, s2:str):
            s1, s2 = removeSameChars(list(s1), list(s2))
            n=len(s1)
            if n==0: return 0
            firstCharOfS2 = s2[0]
            indices = [i for i in range(n) if s1[i] == firstCharOfS2] # find indices of chars in s1 which is equal to first char of s2
            res=float('inf')
            newListOfS1 = [performSwap(s1, i) for i in indices]
            for newS1 in newListOfS1:
                res=min(res, swapFirstCharOfS1(''.join(newS1), ''.join(s2)))
            return res+1
        def performSwap(li,i):
            li = [x for x in li]
            li[0],li[i]=li[i],li[0]
            return li

        return swapFirstCharOfS1(s1,s2)

class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().kSimilarity(s1 = "ab", s2 = "ba"))
    def test2(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "abc", s2 = "bca"))
    def test3(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "abac", s2 = "baca"))
    def test4(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "aabc", s2 = "abca"))
    def test5(self):
        self.assertEqual(1, get_sol().kSimilarity("cba", "abc"))
    def test6(self):
        self.assertEqual(3, get_sol().kSimilarity("bccaba", "abacbc"))
    def test7(self):
        self.assertEqual(3, get_sol().kSimilarity("aabccb", "bbcaca"))
    def test8(self):
        self.assertEqual(11, get_sol().kSimilarity("accbadbbacadcdedaebc", "caeacbbacddceacadbbd"))
