from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def longestDecomposition(self, text: str) -> int:
        @cache
        def dp(idx):
            if idx>n-idx-1:
                return 0
            res=0
            ch=text[idx]
            ch_i=0
            found=False
            while pos[ch][ch_i]<idx:
                ch_i+=1
            iCopy=pos[ch][ch_i]
            jStart=bisect_right(pos[ch],iCopy)
            while jStart<len(pos[ch]) and pos[ch][jStart]<n-idx:
                j=pos[ch][jStart]
                i=iCopy
                if j<=i:
                    continue
                if j>=n-idx:
                    break
                while i<n-i-1 and j<n-idx and text[i]==text[j]:
                    i+=1
                    j+=1
                if j==n-idx:
                    ans=2+dp(i)
                    res=max(res,ans)
                    found=True
                    break
                if found:
                    break
                jStart+=1
            return max(res,1)

        n=len(text)
        pos=defaultdict(list)
        for i,a in enumerate(text): pos[a].append(i)
        res=dp(0)
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(5,get_sol().longestDecomposition("ghiabcadamabcghi"))
    def test02(self):
        self.assertEqual(1,get_sol().longestDecomposition("merchant"))
    def test03(self):
        self.assertEqual(11,get_sol().longestDecomposition("antaprezatepzapreanta"))
    def test04(self):
        self.assertEqual(3,get_sol().longestDecomposition("helloadamhello"))
    def test05(self):
        self.assertEqual(2,get_sol().longestDecomposition("abcabc"))
    def test06(self):
        self.assertEqual(4,get_sol().longestDecomposition("ghiabcabcghi"))
    def test07(self):
        self.assertEqual(7,get_sol().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
    def test08(self):
        self.assertEqual(1000,get_sol().longestDecomposition("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
