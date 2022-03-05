from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# similar to 76

class Solution:
    # required['a]=-1 means: we have more 'a's than we need
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def enough():
            ans=all(required[x]<=0 for x in string.ascii_lowercase)
            return ans
        def valid():
            ans=all(required[x]==0 for x in string.ascii_lowercase)
            return ans

        n=len(s)
        required=Counter()
        for x in p:
            required[x]+=1

        res=[]
        i,j=0,0
        while i<=j:
            while j<n and not enough():
                required[s[j]]-=1
                j+=1
            if valid():
                res.append(i)
            if i<j:
                required[s[i]]+=1
            i+=1
        return res
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):return []
        required = defaultdict(int)
        res,found = [],0
        for c in p:
            required[c]+=1
        for i in range(len(p)-1):
            right_char=s[i]
            if required[right_char]>0:found+=1
            else:found-=1
            required[right_char]-=1
        for i in range(len(p)-1,len(s)):
            right_char = s[i]
            if required[right_char]>0:found+=1
            else:found-=1
            required[right_char]-=1
            if found==len(p):
                 res.append(i-len(p)+1)
            left_char = s[i-len(p)+1]
            required[left_char]+=1
            if required[left_char]>0:found-=1
            else:found+=1
        return res
class Solution3:
    # TLE
    def findAnagrams(self, s: str, p: str) -> List[int]:
        di,res = {},[]
        for c in p:
            if c not in di:di[c]=1
            else:di[c]+=1
        def helper(sub_s,di):
            n = len(sub_s)
            for i in range(n):
                c = sub_s[i]
                if c not in di or di[c]==0:
                    return False
                else:
                    di[c]-=1
            return True
        def get_new_di(di):
            new_di = {}
            for k in di:
                new_di[k]=di[k]
            return new_di
        m,n=len(s),len(p)
        for i in range(m-n+1):
            sub_s = s[i:i+n]
            temp_di = get_new_di(di)
            if helper(sub_s,temp_di):
                res.append(i)
        return res

class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,6],get_sol().findAnagrams("cbaebabacd", "abc"))
    def test2(self):
        self.assertEqual([0,1,2],get_sol().findAnagrams('abab','ab'))
    def test3(self):
        self.assertEqual([],get_sol().findAnagrams("aaaaaaaaaa","aaaaaaaaaaaaa"))
    # def test4(self):
    # def test5(self):


# class mycase(unittest.TestCase):
#     def test1(self):
#         self.assertEqual('BANC', Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
#     def test2(self):
#         self.assertEqual('a', Solution().minWindow(s = "a", t = "a"))
#     def test3(self):
#         self.assertEqual('', Solution().minWindow(s = "a", t = "b"))

