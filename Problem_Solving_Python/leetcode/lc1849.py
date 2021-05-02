import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()
class Solution:
    def splitString(self, s: str) -> bool:
        def helper(s,prev,cnt):
            if not s:
                if cnt<2: return False
                return True
            for i in range(1,len(s)+1):
                first,second = s[:i],s[i:]
                if prev==None or int(first)==prev-1:
                    if helper(second,int(first),cnt+1):
                        return True
            return False

        return helper(s,None,0)



class tester(unittest.TestCase):
    def test1(self):
        s = "1234"
        Output= False
        self.assertEqual(Output,get_sol_obj().splitString(s))
    def test2(self):
        s = "050043"
        Output= True
        self.assertEqual(Output,get_sol_obj().splitString(s))
    def test3(self):
        s = "9080701"
        Output= False
        self.assertEqual(Output,get_sol_obj().splitString(s))
    def test4(self):
        s = "10009998"
        Output= True
        self.assertEqual(Output,get_sol_obj().splitString(s))
