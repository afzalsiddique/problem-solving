from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# use this compressed version
# https://leetcode.com/problems/longest-common-subpath/discuss/1314316/Python-2-solutions%3A-Rolling-Hash-and-Suffix-Array-explained.
def RabinKarp(arr, M, q): # M=window size
    h, t, d = (1<<(17*M-17))%q, 0, 1<<17
    all_hashes = set()

    for i in range(M):
        t = (d * t + arr[i])% q

    all_hashes.add(t)

    for i in range(len(arr) - M):
        t = (d*(t-arr[i]*h) + arr[i + M])% q
        all_hashes.add(t)

    return all_hashes
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def myord(ch):
            if ch=='A': return 1
            if ch=='C': return 2
            if ch=='G': return 3
            return 4

        m=len(s)
        if m<11: return []
        b=4 # base
        p=10**9+7 # prime
        n=10 # len of DNA. window size
        h=(b**(n-1))%p
        freq=Counter()
        indices={} # start index
        w=0 # window hash value
        for i,c in enumerate(s):
            w=((w*b)+myord(c))%p
            if i>=n-1:
                freq[w]+=1
                start=i-n+1
                indices[w]=start
                w=(w-h*myord(s[start]))%p
        res=[]
        for key in freq:
            if freq[key]>1:
                start=indices[key]
                res.append(s[start:start+10])
        return res

class Solution2:
    # time O(10*len(DNA)). space O(len(DNA)/10)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        di=defaultdict(int)
        res=[]
        for i in range(len(s)-10+1):
            di[s[i:i+10]]+=1
        for seq in di:
            if di[seq]>1: res.append(seq)
        return res
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(["AAAAACCCCC","CCCCCAAAAA"],get_sol().findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    def test2(self):
        self.assertEqual(["AAAAAAAAAA"],get_sol().findRepeatedDnaSequences(s = "AAAAAAAAAAAAA"))
    def test3(self):
        self.assertEqual([],get_sol().findRepeatedDnaSequences(s = "A"))
    def test4(self):
        self.assertEqual(["TGAGGATTCT"],get_sol().findRepeatedDnaSequences(s = "GCCTCAAGCTATCCTAATTTGCCTGTTCTACTCTGAGTCTCACAAGCTCCCTGGGGGGCCGAACGGACTCGCAGCTTCACGATTAATGAATGTTTCGACAATGAACTTCCTGTGACGAATCTTTGCCGAGCACGGTCTAGCACTATGAGGATTCTCTTCCCGTGTACTCAACGCGGCACATGTTGGAGGTCACCTCGCCGAGCTACCTGTACCCGGGTCTGTAATTCGGATAATTCAGCTAGGGAGCAAATGTGCAGTCAGAGCTTAAGGTACTTCATGTCGCCTTCGCCTGAAGTCCCTTCTTGCACATTATATCCGTTTTGAGGATTCTACTGATAGATAGGGCGCAAACCTCGTTGACGCCCACGACCAAGGATGGTTACTTTTTACAATATGGAATGCACGAGACCGATTCCGGCCCAGAGGAAAGATTCAAGTCTAAGTAAGCACGGCATGAGGCGCTACGCACCCTTGCCCATGACCCCGCAACGGGAACTATGGCCCCGCGGCATGCGTTATACATTATTAACCCACCGCAGCACCCCCGGACTATTCACGCCAAGTGAGGGATTTATCGATTGGACCCTAGGGGGACTGGCGAGCCGTCTTCCTCGGGAGCGGGGTGGAGTGTTGAACTCGACTCACTATGATAACCGTGTCCACCATCAATGGAAGTGAACCCGCGAGCATCATGCTTTATCCAAATTCGACCACTATCGTTTGTATATGATGACCTTGTATCACTGGCTGGCAGTGGTAACGCTTTAAGCCGTTGTAATATAGAGTCCGCGATATTCACTGACCCTGTTTCCTCAAACCCTTCTCTCGTAAAATAGTGGTGCCCACTCCTTCGGAGTTGGAGAGGTTGATCGTGTCAGAATGACGTCACGGTCACGCAACACTTCTATCTTGGCGAGCACCGCATCTCATGTACCCTTCGTATAGTTAGAGGGTAAGATGTGTCAGCCTCCAAACGAAGTGAACTGTAAAGTGTTCGCCT"))
    # def test4(self):
    #     self.assertEqual(Output,get_sol().findRepeatedDnaSequences(s = "banana"))
