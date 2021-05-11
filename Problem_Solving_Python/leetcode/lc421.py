import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
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
            if opp_bit in node.children:
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

class tester(unittest.TestCase):
    def test01(self):
        nums = [3,10,5,25,2,8]
        Output= 28
        self.assertEqual(Output,Solution().findMaximumXOR(nums))
    def test02(self):
        nums = [0]
        Output= 0
        self.assertEqual(Output,Solution().findMaximumXOR(nums))
    def test03(self):
        nums = [2,4]
        Output= 6
        self.assertEqual(Output,Solution().findMaximumXOR(nums))
    def test04(self):
        nums = [8,10,2]
        Output= 10
        self.assertEqual(Output,Solution().findMaximumXOR(nums))
    def test05(self):
        nums = [14,70,53,83,49,91,36,80,92,51,66,70]
        Output= 127
        self.assertEqual(Output,Solution().findMaximumXOR(nums))
