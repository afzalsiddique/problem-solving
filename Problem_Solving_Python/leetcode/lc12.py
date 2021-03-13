import math
import unittest
from bisect import *
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        val = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        before = {'I':'VX','X':'LC','C':'DM'}
        for sym in before:
            for x in before[sym]:
                val[str(sym)+str(x)] = val[x] - val[sym]
        tuples = []
        for key in val:
            tuples.append((val[key],key))
        tuples.sort()
        values = [tu[0] for tu in tuples]
        letters = [tu[1] for tu in tuples]
        result = []
        while num!=0:
            idx = bisect_left(values, num)
            if idx!=len(values) and values[idx]==num:
                result.append(letters[idx])
                break
            idx-=1
            result.append(letters[idx])
            num-=values[idx]
        return "".join(result)

class Case(unittest.TestCase):
    def test_1(self):
        a = Solution().intToRoman(1234)
        e = 'MCCXXXIV'
        self.assertEqual(e,a)
    def test_2(self):
        a = Solution().intToRoman(1994)
        e = "MCMXCIV"
        self.assertEqual(e,a)
    def test_3(self):
        a = Solution().intToRoman(1)
        e = "I"
        self.assertEqual(e,a)
    def test_4(self):
        a = Solution().intToRoman(58)
        e = "LVIII"
        self.assertEqual(e,a)
