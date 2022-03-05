import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # The key point: reduce right by removing the rightest '1' bit until left<=right;
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            right=right & (right-1)
        return right
class Solution2:
    # https://www.youtube.com/watch?v=-qrpJykY2gE&t=477s
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt=0
        while left!=right:
            left=left>>1
            right=right>>1
            cnt+=1
        return left<<cnt
class Solution3:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        def get_bin(num):
            bin_num = bin(num)[2:]
            bin_num = '0'*(BIG-len(bin_num))+bin_num
            return bin_num
        BIG = 31
        x = 1
        bin_left = get_bin(left)
        res = ['-1']*BIG
        for i in range(BIG-1,-1,-1):
            if bin_left[i]=='0':
                res[i]='0'
            else:
                tmp = min(right,left+x)
                bin_tmp = get_bin(tmp)
                if bin_tmp[i]=='0':
                    res[i]='0'
                else:
                    res[i]='1'
            x*=2
        res = ''.join(res)
        return int(res,2)



class MyTestCase(unittest.TestCase):
    def test1(self):
        left,right = 5,  7
        Output= 4
        self.assertEqual(Output, get_sol().rangeBitwiseAnd(left,right))
    def test2(self):
        left,right = 0,  0
        Output= 0
        self.assertEqual(Output, get_sol().rangeBitwiseAnd(left,right))
    def test3(self):
        left,right = 1,  2147483647
        Output= 0
        self.assertEqual(Output, get_sol().rangeBitwiseAnd(left,right))
    def test4(self):
        left,right = 20000, 2147483647
        Output= 0
        self.assertEqual(Output, get_sol().rangeBitwiseAnd(left,right))
    # def test5(self):
    # def test6(self):
    # def test7(self):
