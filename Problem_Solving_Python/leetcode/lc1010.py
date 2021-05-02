import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()
# https://www.youtube.com/watch?v=toYgBIaUdfM&t=163s
# https://www.youtube.com/watch?v=wxqN1HX4Djk
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def sum_upto_n(n):
            sum = 0
            for i in range(1,n+1):
                sum+=i
            return sum
        count = [0]*60
        for t in time:
            count[t%60]+=1
        total=0
        for i in range(1,30):
            total+= count[i]* count[60-i]
        total+=sum_upto_n(count[0]-1)
        total+=sum_upto_n(count[30]-1)
        return total

class tester(unittest.TestCase):
    def test1(self):
        time = [30,20,150,100,40]
        Output= 3
        self.assertEqual(Output,get_sol_obj().numPairsDivisibleBy60(time))
