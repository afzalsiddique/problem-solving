from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def merge(self,s1:str,s2:str)->str:
        cut=min(len(s1),len(s2))
        for i in range(cut,0,-1):
            lastS1=s1[-i:]
            firstS2=s2[:i]
            if lastS1==firstS2:
                return s1+s2[i:]
        return s1+s2
    def shortestSuperstring(self, words: List[str]) -> str:
        def turn_on(mask,i): return mask | (1<<i)
        def is_on(mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        @cache
        def backtrack(mask:int,path:str):
            nonlocal res
            if allSelected(mask,n):
                res=min(res,path,key=lambda x:len(x))
                return
            for i in range(n):
                if is_on(mask,i): continue
                newMask = turn_on(mask,i)
                backtrack(newMask,self.merge(path,words[i]))

        n=len(words)
        res='a'*(20*12+1)
        backtrack(0,'')
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertIn(get_sol().shortestSuperstring(["alex","loves","leetcode"]),["alexlovesleetcode","leetcodelovesalex","lovesleetcodealex"])
    def test2(self):
        self.assertIn(get_sol().shortestSuperstring(["gcta","ctaagt","catg","ttca"]),["gctaagttcatg","ttcatgctaagt"])
    def test3(self):
        self.assertIn(get_sol().shortestSuperstring(["abcd","bcde"]),["abcde"])
    def test4(self):
        self.assertIn(get_sol().shortestSuperstring(["a"]),["a"])
    def test5(self):
        self.assertIn(get_sol().shortestSuperstring(["cmqitnqwahfl","ygeeoensdpuobhazkn","fxlqkqwemwhpeoblldcv","eoblldcvypdygeeoen","dpuobhazknowcmq","yfhctxzvfxlqkqwemwh","emwhpeoblldcvypdygee","dcvypdygeeoensdpuobh","zvfxlqkqwemwhpeobl"]),["yfhctxzvfxlqkqwemwhpeoblldcvypdygeeoensdpuobhazknowcmqitnqwahfl"])
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
