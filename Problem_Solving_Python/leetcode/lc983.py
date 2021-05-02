import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp = {}
        def helper(i,day):
            if i==n: return 0
            if (i,day) in dp: return dp[(i,day)]
            if days[i]<day:
                ans = helper(i+1,day)
            else:
                option1 = costs[0]+helper(i+1,days[i]+1)
                option2 = costs[1]+helper(i+1,days[i]+7)
                option3 = costs[2]+helper(i+1,days[i]+30)
                ans = min(option1,option2,option3)
            dp[(i,day)]=ans
            return ans
        return helper(0,0)



class tester(unittest.TestCase):
    def test1(self):
        days = [1,4,6,7,8,20]
        costs = [2,7,15]
        Output= 11
        self.assertEqual(Output,get_sol_obj().mincostTickets(days,costs))
    def test2(self):
        days = [1,2,3,4,5,6,7,8,9,10,30,31]
        costs = [2,7,15]
        Output= 17
        self.assertEqual(Output,get_sol_obj().mincostTickets(days,costs))
