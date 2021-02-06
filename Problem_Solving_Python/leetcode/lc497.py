# https://www.youtube.com/watch?v=8kwPXbTMSnk
# *****WRONG******
import unittest
from bisect import bisect_left
from random import randint
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.cumulative_sum = []
        # self.di=[] # key:cumulative_sum, value:rect
        self.calculate_cumulative_sum()

    def pick(self) -> List[int]:
        rand_int = randint(1, self.cumulative_sum[-1])
        rect_idx = bisect_left(self.cumulative_sum, rand_int)
        if rect_idx == 0:
            point = rand_int
        else:
            point = rand_int - self.cumulative_sum[rect_idx-1]
        cordinate = self.get_cordinate(self.rects[rect_idx], point)
        return cordinate

    def get_cordinate(self, rect, point):
        x1, y1, x2, y2 = rect
        no_of_rows = (y2 - y1 + 1)
        row = point // no_of_rows
        row += x1
        col = point % no_of_rows
        col += y1
        return [row, col]

    def calculate_cumulative_sum(self):
        first_area = self.get_area(self.rects[0])
        self.cumulative_sum = [first_area]
        # self.di[first_area] = self.rects[0]
        for i in range(1, len(self.rects)):
            last_sum = self.cumulative_sum[-1]
            area = self.get_area(self.rects[i])
            self.cumulative_sum.append(last_sum + area)
            # self.di[area] = self.rects[i]

    def get_area(self, rect):
        x1, y1, x2, y2 = rect
        rows = (y2 - y1) + 1
        cols = (x2 - x1) + 1
        area = rows * cols
        return area

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution([[1,1,2,2]])
        di = {}
        for _ in range(10000):
            cordinate = tuple(sol.pick())
            if cordinate in di:
                di[cordinate]+=1
            else:
                di[cordinate]=1
        expected = {(1,1):2500,(1,2):2500,(2,1):2500,(2,2):2500}
        actual = di
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution([[-1,-1,0,1]])
        di = {}
        for _ in range(10000):
            cordinate = tuple(sol.pick())
            if cordinate in di:
                di[cordinate]+=1
            else:
                di[cordinate]=1
        expected = {(-1,-1):1667,(-1,0):1667,(-1,1):1667,(0,-1):1667,(0,0):1667, (0,1):1667}
        actual = di
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)