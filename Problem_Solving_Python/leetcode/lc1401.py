import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def check_inside_circle(x,y): # distance between center and point should less than radius. Square root can be avoided.
            x_diff,y_diff=x_center-x,y_center-y
            return x_diff*x_diff+y_diff*y_diff <= radius*radius
        # if center of the circle inside rectangle
        if x1<=x_center<=x2 and y1<=y_center<=y2:
            return True
        # check if any points in the border inside the circle
        for x in range(x1,x2+1):
            y=y1
            if check_inside_circle(x,y):
                return True
        for x in range(x1,x2+1):
            y=y2
            if check_inside_circle(x,y):
                return True
        for y in range(y1,y2+1):
            x=x1
            if check_inside_circle(x,y):
                return True
        for y in range(y1,y2+1):
            x=x2
            if check_inside_circle(x,y):
                return True
        return False

class MyTestCase(unittest.TestCase):
    def test_1(self):
        radius,x_center,y_center,x1,y1,x2,y2 = 1,  0,  0,  1,  -1,  3,  1
        Output= True
        self.assertEqual(Output, get_sol().checkOverlap(radius,x_center,y_center,x1,y1,x2,y2))
    def test_2(self):
        radius,x_center,y_center,x1,y1,x2,y2 = 1,  0,  0,  -1,  0,  0,  1
        Output= True
        self.assertEqual(Output, get_sol().checkOverlap(radius,x_center,y_center,x1,y1,x2,y2))
    def test_3(self):
        radius,x_center,y_center,x1,y1,x2,y2 = 1,  1,  1,  -3,  -3,  3,  3
        Output= True
        self.assertEqual(Output, get_sol().checkOverlap(radius,x_center,y_center,x1,y1,x2,y2))
    def test_4(self):
        radius,x_center,y_center,x1,y1,x2,y2 = 1,  1,  1,  1,  -3,  2,  -1
        Output= False
        self.assertEqual(Output, get_sol().checkOverlap(radius,x_center,y_center,x1,y1,x2,y2))
    def test_5(self):
        radius,x_center,y_center,x1,y1,x2,y2 = 5, 8, 8, 9, 5, 12, 8
        Output= True
        self.assertEqual(Output, get_sol().checkOverlap(radius,x_center,y_center,x1,y1,x2,y2))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
