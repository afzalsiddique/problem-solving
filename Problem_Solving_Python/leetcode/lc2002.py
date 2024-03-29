import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/discuss/1458544/Python-Clean-and-Simple-bitmask
    def maxProduct(self, s: str) -> int:
        def isSelected(mask, i): return mask & (1 << i)
        def cartesian_product(li1,li2):
            # return [((mask1,len1),(mask2,len2)) for mask1,len1 in li1 for mask2,len2 in li2] # list gives tle
            return (((mask1,len1),(mask2,len2)) for mask1,len1 in li1 for mask2,len2 in li2) # change it to generator

        n = len(s)
        arr = [] # contains tuple(valid palindrome mask, len(palindrome)

        for mask in range(1, 1<<n): # palindrome of len 0 gives product 0
            subseq = []
            for i in range(n): # convert the bitmask to the actual subsequence
                if isSelected(mask,i):
                    subseq.append(s[i])
            if subseq == subseq[::-1]: # if palindrome
                arr.append((mask, len(subseq)))
                # arr.append((mask, len(subseq),subseq))

        result = 1
        for (mask1, len1), (mask2, len2) in cartesian_product(arr, arr):
            if mask1 & mask2 == 0: # disjoint
                result = max(result, len1 * len2)
        return result
class Solution2:
    # tle. same as Solution3() but with mask
    def maxProduct(self, s: str) -> int:
        def turnOn(mask, i): return mask | (1 << i)
        def get_text(mask): # given mask return the actual text
            b = bin(mask)[2:]
            n=len(b)
            li = [n-int(i)-1 for i in range(n) if b[i]=='1']
            txt = []
            for i in li:
                txt.append(s[i])
            return txt
        def isPalindrome(txt): return txt==txt[::-1]

        def backtrack(start, state1, state2):
            if start==n:
                txt1 = get_text(state1)
                txt2 = get_text(state2)
                if isPalindrome(txt1) and isPalindrome(txt2):
                    return len(txt1) * len(txt2)
                return float('-inf')
            if (start,state1,state2) in dp: return dp[start,state1,state2]
            maxx=float('-inf')
            for i in range(start,n):
                option1=backtrack(i + 1, turnOn(state1,i), state2)
                option2=backtrack(i + 1, state1, turnOn(state2,i))
                option3=backtrack(i + 1, state1, state2)
                maxx=max(maxx,option1,option2,option3)
            dp[start,state1,state2] = maxx
            return maxx

        n=len(s)
        dp={}
        return backtrack(0,0,0)
class Solution3:
    # tle
    def maxProduct(self, s: str) -> int:
        def isPalindrome(s): return s==s[::-1]
        def backtrack(start,path1,path2):
            if start==n:
                if isPalindrome(path1) and isPalindrome(path2):
                    return len(path1)*len(path2)
                return float('-inf')
            maxx=float('-inf')
            for i in range(start,n):
                option1= backtrack(i+1,path1+[s[i]],path2) # take the ith char to string1
                option2 = backtrack(i+1,path1,path2+[s[i]]) # take the ith char to string2
                option3 = backtrack(i+1,path1,path2) # skip the ith char
                maxx=max(maxx,option1,option2,option3)
            return maxx

        n=len(s)
        return backtrack(0,[],[])

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(9, get_sol().maxProduct("leetcodecom"))
    def test02(self):
        self.assertEqual(1, get_sol().maxProduct("bb"))
    def test03(self):
        self.assertEqual(25, get_sol().maxProduct("accbcaxxcxx"))
    def test04(self):
        self.assertEqual(10, get_sol().maxProduct("nphnphmpm"))
    def test05(self):
        self.assertEqual(20, get_sol().maxProduct("wgtniiotgw"))
    def test06(self):
        self.assertEqual(20, get_sol().maxProduct("nggaagugnk"))
    def test07(self):
        self.assertEqual(12, get_sol().maxProduct("rssuwyvvyw"))
    def test08(self):
        self.assertEqual(25, get_sol().maxProduct("dyfctcfytd"))
    def test09(self):
        self.assertEqual(30, get_sol().maxProduct("fffffffffff"))
    def test10(self):
        self.assertEqual(35,get_sol().maxProduct("aapdapapaapp"))
