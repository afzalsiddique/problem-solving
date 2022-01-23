from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; import functools
from binary_tree_tester import *
# if opposite value exits then xor it opposite bit to get highest value -> 0^1=1
def get_sol(): return Solution()
class Trie:
    def __init__(self):
        self.root = {}
        self.maxLen=32
    def insert(self, num):
        node = self.root
        for i in range(self.maxLen, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, num):
        node = self.root
        if not node: return -1
        res=0
        for i in range(self.maxLen, -1, -1):
            bit = (num >> i) & 1
            if 1 - bit in node:
                node = node[1 - bit]
                res |= (1 << i)
            else:
                node = node[bit]
        return res
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Trie()
        for x in nums:
            trie.insert(x)
        res=float('-inf')
        for x in nums:
            res=max(res,trie.query(x))
        return res
class Trie2:
    class Node:
        def __init__(self):
            self.children={}
        def __repr__(self): return str(self.children)
    def __init__(self,nums):
        self.root=Trie2.Node()
        # self.maxLen=32 # should also work
        self.maxLen=max(nums,key=lambda x:x.bit_length()).bit_length()
        for num in nums:
            self.insert(num)
    def insert(self, num: int) -> None:
        num= bin(num)[2:]
        if len(num)<self.maxLen:
            padding=self.maxLen-len(num)
            num= '0' * padding + num
        node=self.root
        for c in num:
            if c not in node.children:
                node.children[c]=Trie2.Node()
            node=node.children[c]
    def getMaxXor(self,num:int):
        num=bin(num)[2:]
        if len(num)<self.maxLen:
            padding=self.maxLen-len(num)
            num= '0' * padding + num
        node=self.root
        li=[]
        for c in num:
            opp='0' if c=='1' else '1'
            if opp in node.children:
                li.append(opp)
                node=node.children[opp]
            else:
                li.append(c)
                node=node.children[c]
        res=int(''.join(li),2)^int(num,2)
        return res
class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Trie2(nums)
        return max(trie.getMaxXor(num) for num in nums)
class Solution3:
    # https://www.youtube.com/watch?v=wSgrc98d2lI
    # THE MAXIMUM XOR WILL BE AS MANY ONES TO THE LEFT Let us try to
    class TrieNode:
        def __init__(self):
            self.children = {}
            # isEnd not required because all the nums are of same length
        def __repr__(self): return str(self.children)

    def __init__(self):
        self.root=self.TrieNode()
    def insert(self,num):
        bits_num = bin(num) # 0b10101 # convert to binary
        bits_num = bits_num[2:] # 10101 # remove '0b'
        bits_num= bits_num.zfill(32) # 0000..10101 # fill it with zeros at the beginning
        node = self.root
        for bit in bits_num:
            if bit not in node.children:
                node.children[bit]=self.TrieNode()
            node = node.children[bit]

    def find_max_xor(self,num):
        node = self.root
        max_xor=''
        bits_num = bin(num)
        bits_num = bits_num[2:]
        bits_num = bits_num.zfill(32)
        for bit in bits_num:
            if bit =='0':
                opp_bit = '1'
            else:
                opp_bit = '0'
            if opp_bit in node.children: # when we have 0 and 1 get highest value-> 0^1=1
                max_xor+=opp_bit
                node=node.children[opp_bit]
            else:
                max_xor+=bit
                node=node.children[bit]
        max_xor = int(max_xor,2) # convert to integer given a base-2 num
        return max_xor ^ num

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)
        max_xor=0
        for num in nums:
            max_xor = max(max_xor,self.find_max_xor(num))
        return max_xor

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(28,get_sol().findMaximumXOR([3,10,5,25,2,8]))
    def test02(self):
        self.assertEqual(0,get_sol().findMaximumXOR([0]))
    def test03(self):
        self.assertEqual(6,get_sol().findMaximumXOR([2,4]))
    def test04(self):
        self.assertEqual(10,get_sol().findMaximumXOR([8,10,2]))
    def test05(self):
        self.assertEqual(127,get_sol().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
