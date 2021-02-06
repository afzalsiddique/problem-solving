# https://www.youtube.com/watch?v=fWS0TCcr-lE
import unittest
from bisect import bisect_left
from random import randint
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.cumulative_sum = [self.w[0]] # cumulative sum
        for i in range(1, len(self.w)):
            self.cumulative_sum.append(self.cumulative_sum[-1] + self.w[i])
    def pickIndex(self) -> int:
        rand_int = randint(1, self.cumulative_sum[-1])
        idx = bisect_left(self.cumulative_sum, rand_int)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution([1,3,6])
        di = {}
        for _ in range(10000):
            idx = sol.pickIndex()
            if idx in di:
                di[idx]+=1
            else:
                di[idx]=1
        print(di)
        expected = {0:1000,1:3000,2:6000}
        actual = di
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution([1])
        di = {}
        for _ in range(10000):
            idx = sol.pickIndex()
            if idx in di:
                di[idx]+=1
            else:
                di[idx]=1
        print(di)
        expected = {0:10000}
        actual = di
        self.assertEqual(expected, actual)

