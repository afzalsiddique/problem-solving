from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# similar to 76
class Solution:
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
    # TLE
    def findAnagrams_(self, s: str, p: str) -> List[int]:
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
        self.assertEqual([0,6],Solution().findAnagrams("cbaebabacd", "abc"))
    def test2(self):
        self.assertEqual([0,1,2],Solution().findAnagrams('abab','ab'))
    def test3(self):
        self.assertEqual([],Solution().findAnagrams("aaaaaaaaaa","aaaaaaaaaaaaa"))
    # def test4(self):
    # def test5(self):


# class mycase(unittest.TestCase):
#     def test1(self):
#         self.assertEqual('BANC', Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
#     def test2(self):
#         self.assertEqual('a', Solution().minWindow(s = "a", t = "a"))
#     def test3(self):
#         self.assertEqual('', Solution().minWindow(s = "a", t = "b"))

