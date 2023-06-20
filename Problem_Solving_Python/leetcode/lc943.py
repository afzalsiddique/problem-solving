from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution2()
class Solution:
    # https://www.youtube.com/watch?v=-JjA4BLQyqE
    # https://leetcode.com/problems/find-the-shortest-superstring/discuss/194932/Travelling-Salesman-Problem
    def shortestSuperstring(self, A: List[str]) -> str:
        def turn_off(mask, i): return mask & ~(1 << i)
        def is_on(mask,i): return mask & (1<<i)
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        def calc(a:str,b:str): # a='abcd',b='bcde'-> return 1. add 1 more char to str a to get str (a+b).
            for i in range(1,len(a)):
                if b.startswith(a[i:]):
                    return len(b)-len(a)+i
            return len(b)

        n=len(A)
        graph = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                graph[i][j]=calc(A[i],A[j])
                graph[j][i]=calc(A[j],A[i])
        dp = [[float('inf')]*n for _ in range(1<<n)]
        path = [[0]*n for _ in range(1<<n)]
        last=-1
        minn=float('inf')

        # tsp-dp
        for mask in range(1,1<<n):
            for j in range(n):
                if not is_on(mask,j): # j is not in the set of selected nodes
                    continue
                prev=turn_off(mask,j)
                if prev==0: # if this is the only word
                    dp[mask][j]=len(A[j]) # take the whole word
                else:
                    for k in range(n):
                        if dp[prev][k]+graph[k][j]<dp[mask][j]:
                            dp[mask][j]=dp[prev][k]+graph[k][j]
                            path[mask][j]=k
                if allSelected(mask,n) and dp[mask][j]<minn:
                    minn=dp[mask][j]
                    last=j
        # build the path
        res = []
        cur = (1 << n) - 1
        stack=[]
        while cur>0:
            stack.append(last)
            temp=cur
            cur = turn_off(cur,last)
            last = path[temp][last]

        # build the result
        i = stack.pop()
        res.append(A[i])
        while stack:
            j = stack.pop()
            res.append(A[j][-graph[i][j]:])
            i = j
        return ''.join(res)
class Solution2:
    # https://www.youtube.com/watch?v=LGtMbNbzOC0
    def shortestSuperstring(self, words: List[str]) -> str:
        def turn_on(mask,i): return mask | (1<<i)
        def is_on(mask,i): return mask & (1<<i)
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        def overlapAppend(a:str,b:str):
            for i in range(len(a)):
                if b.startswith(a[i:]):
                    return a[:i]+b
            return a+b
        @cache
        def shortestSuperstring(startWord: str, mask: int):
            if allSelected(mask,n):
                return startWord
            shortest = None
            for i in range(len(words)):
                if not is_on(mask, i):
                    superstring = shortestSuperstring(words[i], turn_on(mask, i))
                    appended = overlapAppend(startWord,superstring)
                    if shortest is None or len(appended)<len(shortest):
                        shortest = appended
            return shortest

        n=len(words)
        mask = 0
        return shortestSuperstring("", mask)
class Solution3:
    def merge(self,s1:str,s2:str)->str:
        cut=min(len(s1),len(s2))
        for i in range(cut,0,-1):
            lastS1=s1[-i:]
            firstS2=s2[:i]
            if lastS1==firstS2:
                return s1+s2[i:]
        return s1+s2
    def mergeAll(self, indices:tuple[int],words:List[str]):
        s=''
        for i in indices:
            s=self.merge(s,words[i])
        return s
    def shortestSuperstring(self, words: List[str]) -> str:
        def turn_on(mask,i): return mask | (1<<i)
        def is_on(mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        def backtrack(mask:int,path:tuple[int]):
            nonlocal res
            if allSelected(mask,n):
                s = self.mergeAll(path,words)
                res=min(res,s,key=lambda x:len(x))
                return
            for i in range(n):
                if is_on(mask,i): continue
                newMask = turn_on(mask,i)
                backtrack(newMask,tuple(list(path)+[i]))

        n=len(words)
        res='a'*(20*12+1)
        backtrack(0,tuple([]))
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
