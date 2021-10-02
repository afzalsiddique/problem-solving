import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        if n == 1: return binary
        count = Counter(binary)
        zero_count = count['0']
        i=0
        while i < n and binary[i] == '1':
            i += 1
        initial_one_count=i
        remaining_one_count = count['1'] - initial_one_count
        if zero_count == 0 or zero_count == 1: return binary
        return '1' * initial_one_count \
               + '1' * (zero_count - 1) \
               + '0' \
               + '1' * remaining_one_count


class MyTestCase(unittest.TestCase):
    def test_1(self):
        binary, Output = "000110", "111011"
        self.assertEqual(Output, get_sol().maximumBinaryString(binary))

    def test_2(self):
        binary, Output = "01", "01"
        self.assertEqual(Output, get_sol().maximumBinaryString(binary))

    def test_3(self):
        binary, Output = "1100", "1110"
        self.assertEqual(Output, get_sol().maximumBinaryString(binary))
    def test_4(self):
        binary, Output = "101010111011001101000110010001100001111", "111111111111111111101111111111111111111"
        self.assertEqual(Output, get_sol().maximumBinaryString(binary))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
