import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def fallingSquares(self, nums: List[List[int]]) -> List[int]:
        def isOverlapping(s1, e1, s2, e2):
            return max(s1, s2) < min(e1, e2)
        def getMaxHeight(start, end, height):
            maxHeight=0
            for s,e,h in intervals:
                if isOverlapping(start, end, s, e):
                   maxHeight=max(maxHeight,h)
            return maxHeight + height
        intervals= []
        res=[]
        maxHeight=0
        for x,r in nums:
            start,end,height=x,x+r,r
            newHeight=getMaxHeight(start,end,height)
            intervals.append((start,end,newHeight))
            maxHeight=max(maxHeight,newHeight)
            res.append(maxHeight)
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,5], get_sol().fallingSquares([[1,2],[2,3]]))
    def test2(self):
        self.assertEqual([2,5,5], get_sol().fallingSquares([[1,2],[2,3],[6,1]]))
    def test3(self):
        self.assertEqual([100,100], get_sol().fallingSquares([[100,100],[200,100]]))
    def test4(self):
        self.assertEqual([1,10,18], get_sol().fallingSquares([[2,1],[2,9],[1,8]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):

