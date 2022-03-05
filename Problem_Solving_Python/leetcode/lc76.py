from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://leetcode.com/problems/minimum-window-substring/discuss/26810/Java-solution.-using-two-pointers-+-HashMap/260540
# similar to 438

# https://leetcode.com/problems/minimum-window-substring/discuss/226911/Python-two-pointer-sliding-window-with-explanation
# https://www.youtube.com/watch?v=U1q16AFcjKs&t=90s
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        i, j, found = 0, len(s)-1, 0
        min_win = ""
        for j in range(len(s)):
            right_letter = s[j]
            if required[right_letter]>0:found += 1
            required[right_letter] -=1
            while found==len(t):
                left_letter = s[i]
                #print(i, j, required)
                if not min_win or j-i+1<len(min_win):
                    min_win = s[i:j+1]
                required[left_letter]+=1
                if required[left_letter]>0:found -=1
                i+=1
        return min_win

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:return ""
        di,missing = defaultdict(int), len(t)
        ans = float("inf"), None, None
        l,r = 0,0
        for letter in t:
            di[letter]+=1
        while r < len(s):
            c_right = s[r]
            if c_right in di:
                di[c_right]-=1 # negative value in the dict means extra characters or useless characters are inside window. s='ABBBC', t = 'ABC'. Here  at some point di['B']=-2.
                if di[c_right] >= 0: # found a useful char.
                    missing-=1
            # if found a susbtring
            while not missing and l <= r:
                cur_len = r - l + 1
                if cur_len < ans[0]:
                    ans = (r-l+1,l,r)
                # move left_pointer to the right
                c_left = s[l]
                if c_left in di:
                    di[c_left] += 1
                    if di[c_left] >= 1: # a useful char will be removed
                        missing+=1
                l+=1
            r+=1
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]
class Solution3:
    # required['a]=-1 means: we have more 'a's than we need
    def minWindow(self, s: str, t: str) -> str:
        LETTERS=string.ascii_lowercase+string.ascii_uppercase
        def valid():
            ans=all(required[x]<=0 for x in LETTERS)
            return ans

        n=len(s)
        required=Counter()
        for x in t:
            required[x]+=1

        start,end=[0,0]
        res=float('inf')
        i,j=0,0
        while i<=j:
            while j<n and not valid():
                required[s[j]]-=1
                j+=1
            if valid() and j-i<res:
                res=j-i
                start,end=i,j
            if i<j:
                required[s[i]]+=1
            i+=1
        return s[start:end]
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual('BANC', Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
    def test2(self):
        self.assertEqual('a', Solution().minWindow(s = "a", t = "a"))
    def test3(self):
        self.assertEqual('', Solution().minWindow(s = "a", t = "b"))
