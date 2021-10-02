import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # example: n=7
    # Suppose the original array is:                      [   a0,      a1,       a2,       a3,       a4,       a5,       a6]
    # encoded array will be:                              [         a1^a2,    a2^a3,    a3^a4,    a4^a5,    a5^a6,    a6^a7]
    # select or do not select:                            [            no,      yes,       no,      yes,       no,      yes]
    # a0 is the  xor the selected and the original array  [  a0,       a1, a2^a2^a3,       a3, a4^a5^a5,       a5, a6^a6^a7]

    # next part same as https://leetcode.com/problems/decode-xored-array/

    def decode(self, encoded: List[int]) -> List[int]:
        # calculating a0
        a0 = 0
        for i in range(len(encoded)):
            if i&1:
                a0 ^= encoded[i]

        for i in range(1,len(encoded)+2):
            a0 ^= i

        res = [a0]
        for i in range(len(encoded)):
            tmp = res[i]^encoded[i]
            res.append(tmp)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        encoded = [3,1]
        Output= [1,2,3]
        self.assertEqual(Output, get_sol().decode(encoded))
    def test2(self):
        encoded = [6,5,4,6]
        Output= [2,4,1,5,3]
        self.assertEqual(Output, get_sol().decode(encoded))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
