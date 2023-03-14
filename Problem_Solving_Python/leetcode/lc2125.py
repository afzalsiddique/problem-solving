import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        def ifSecurity(row:str):
            return any(x=='1' for x in row)
        def noOfSecurity(row:str):
            return sum(x=='1' for x in row)
        m,n=len(bank),len(bank[0])
        prev=0
        res=0
        for i in range(m):
            if ifSecurity(bank[i]):
                cur=noOfSecurity(bank[i])
                res+=cur*prev
                prev=cur
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(8, get_sol().numberOfBeams(["011001","000000","010100","001000"]))
    def test2(self):
        self.assertEqual(0, get_sol().numberOfBeams(["000","111","000"]))
    # def test3(self):
    #     self.assertEqual(4, get_sol().numberOfBeams())
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
