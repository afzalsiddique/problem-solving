import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # In this approach, you just need to find sections like this
    # X .   .   .   . X
    # i                j
    # Where X can be 'R' or 'L' and in between there can be as many dots
    # Now,
    # - you know the length of mid part
    # - If char[i] == char[j] == 'R', means all go towards right (R)
    # -  char[i]  == char[j] == 'L', means all go towards Left (L)
    # -  If char[i] = 'L' and char[j] = 'R', means middle part is not affected so they remain '.'
    # -  If char[i] = 'R' and char[j] = 'L', then it will affect the middle part.
    #    The middle_part/2 close to i will be affected by 'R' and middle_part/2 close to j will be
    #    effected by 'L'  and the last mid point (middle_part%2) will be unaffected due to equal
    #    force from left and right so it remains '.'
    def pushDominoes(self, dominoes: str) -> str:
        tmp = 'L' + ''.join(dominoes) + 'R'
        dominoes = list(tmp)
        n = len(dominoes)
        left = 0
        right = None
        for i in range(left + 1, n):
            if dominoes[i] in 'LR':
                right = i
                break
        while right < n:
            if dominoes[left] == dominoes[right] == 'L': # dots between left and right should be 'L'
                for i in range(left + 1, right):
                    dominoes[i] = 'L'
            elif dominoes[left] == dominoes[right] == 'R': # dots between left and right should be 'R'
                for i in range(left, right):
                    dominoes[i] = 'R'
            elif dominoes[left] == 'R' and dominoes[right] == 'L': # half of all the dots between left and right should be 'R' and the other half should be 'L'
                new_left = left + 1
                new_right = right - 1
                while new_left < new_right: # '<' because if there are odd no of dots then the middle dot should not change
                    dominoes[new_left] = 'R'
                    dominoes[new_right] = 'L'
                    new_left += 1
                    new_right -= 1
            left = right
            right += 1
            while right < n and dominoes[right] not in 'LR':
                right += 1
        return ''.join(dominoes[1:-1])


class MyTestCase(unittest.TestCase):
    def test_1(self):
        Input = ".L.R...LR..L.."
        Output = "LL.RR.LLRRLL.."
        self.assertEqual(Output, get_sol().pushDominoes(Input))

    def test_2(self):
        Input = "RR.L"
        Output = "RR.L"
        self.assertEqual(Output, get_sol().pushDominoes(Input))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
