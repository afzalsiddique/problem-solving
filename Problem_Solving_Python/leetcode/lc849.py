import unittest
from typing import List
def get_sol_obj(): return Solution2()


class Solution:
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
class Solution2:
    def maxDistToClosest(self, seats):
        n=len(seats)
        start=0
        end=0
        i=0
        middle=0
        for i in range(n): # [0,0,0,1]
            if seats[i]==1:
                break
            start+=1
        cnt=0
        for i in range(i+1,n):
            if seats[i]==1:
                cnt+=1
                middle = max(middle,cnt)
                cnt=0
            else:
                cnt+=1
        end=cnt # [1,0,0,0]
        return max(start,end,middle//2)

class MyTestCase(unittest.TestCase):
    def test_01(self):
        seats = [1,0,0,0,1,0,1]
        Output= 2
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
    def test_02_1(self):
        seats = [1,0,0,0]
        Output= 3
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
    def test_02_2(self):
        seats = [0,0,0,1]
        Output= 3
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
    def test_03_1(self):
        seats = [1,0,0]
        Output= 2
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
    def test_03_2(self):
        seats = [0,0,1]
        Output= 2
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
    def test_04(self):
        seats = [0,1]
        Output= 1
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
    def test_05(self):
        seats = [1,0,0,1]
        Output= 1
        self.assertEqual(Output, get_sol_obj().maxDistToClosest(seats))
