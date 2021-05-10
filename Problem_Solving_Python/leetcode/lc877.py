import unittest
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        to_win=sum(piles)//2+1
        dp = {}
        def helper(left, right, turn, alex, lee):
            if left>right:
                if alex>=to_win: return True
                return False
            if (left,right,turn) in dp: return dp[(left,right,turn)]
            ans = False
            if turn: # if alex's turn
                # pick left
                if helper(left+1, right, not turn, alex + piles[left], lee):
                    ans = True
                # pick right
                if helper(left,right-1, not turn, alex + piles[right], lee):
                    ans = True
            else: # not alex's turn
                if helper(left+1, right, not turn, alex, lee + piles[left]):
                    ans = True
                if helper(left,right-1, not turn, alex, lee + piles[right]):
                    ans = True
            dp[(left,right,turn)] = ans
            return ans

        return helper(0,len(piles)-1,True,0,0)

class MyTestCase(unittest.TestCase):
    def test1(self):
        solution = Solution()
        piles = [5,3,4,5]
        actual = solution.stoneGame(piles)
        expected = True
        self.assertEqual(expected, actual)

    def test2(self):
        solution = Solution()
        piles = [5,3,4,5]
        actual = solution.stoneGame(piles)
        expected = True
        self.assertEqual(expected, actual)
