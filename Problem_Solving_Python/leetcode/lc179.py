from bisect import bisect_left
from collections import deque, defaultdict
from functools import cmp_to_key
from heapq import *
import unittest
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(n1,n2):
            return int(n2+n1)-int(n1+n2)
        if any(nums)==False:
            return "0"
        return "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        if any(nums)==False:
            return "0"
        return "".join(sorted(map(str, nums), key=cmp_to_key(lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0))))

class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual("9534330",Solution().largestNumber([3,30,34,5,9]))