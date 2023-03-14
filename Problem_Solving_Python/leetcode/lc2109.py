from collections import deque;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n=len(s)
        res=[]
        q = deque(spaces)
        i=0
        while i<n:
            if q and q[0]==i:
                res.append(' ')
                q.popleft()
            else:
                res.append(s[i])
                i+=1
        while q:
            res.append(' ')
            q.popleft()
        return ''.join(res)

class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual("This Is Me",get_sol().addSpaces("ThisIsMe",[4,6]))
    def test_2(self):
        self.assertEqual("Enjoy Your Coffee",get_sol().addSpaces("EnjoyYourCoffee",[5,9]))
    def test_3(self):
        self.assertEqual("Leetcode Helps Me Learn",get_sol().addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
    def test_4(self):
        self.assertEqual("i code in py thon",get_sol().addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))
    def test_5(self):
        self.assertEqual(" s p a c i n g",get_sol().addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))
    def test_6(self):
        self.assertEqual(" ",get_sol().addSpaces(s = "", spaces = [0]))
    def test_7(self):
        self.assertEqual("   ",get_sol().addSpaces(s = "", spaces = [0,1,2]))
    # def test_8(self):
    # def test_9(self):
