import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    # tabular dp
    # time O(n^2) space O(n^2)
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in reversed(range(n)):
            for j in range(i+1, n):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        for row in dp:
            print(row)
        return True if dp[0][-1] >= 0 else False





class Solution2:
    # recursive dp
    # time O(n^2) space O(n^2)
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def helper(i, j):
            if i==j:
                return nums[i]
            if (i, j) in dp: return dp[(i, j)]
            option1 = nums[i]-helper(i + 1, j)
            option2 = nums[j]-helper(i, j - 1)
            dp[(i, j)] = max( option1 ,option2 )
            return dp[(i, j)]
        return helper(0,len(nums)-1) >= 0

class Solution3:
    # tle
    # minimax
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def helper(lo,hi,turn,score1):
            if lo>hi:
                return score1
            if (lo,hi,turn) in dp: return dp[(lo,hi,turn)]
            if turn: # player1's turn
                temp1 =helper(lo+1,hi,not turn,score1+nums[lo])
                temp2 = helper(lo,hi-1,not turn,score1+nums[hi])
                if temp1>temp2:
                    return helper(lo+1,hi,not turn,score1+nums[lo])
                else:
                    return helper(lo,hi-1,not turn,score1+nums[hi])
            else: # player2's turn
                temp1 =helper(lo+1,hi,not turn,score1-nums[lo])
                temp2 = helper(lo,hi-1,not turn,score1-nums[hi])
                if temp1<temp2:
                    return helper(lo+1,hi,not turn,score1-nums[lo])
                else:
                    return helper(lo,hi-1,not turn,score1-nums[hi])

        ans = helper(0,len(nums)-1,True,0)
        return ans>=0

class MyTestCase(unittest.TestCase):
    def test01(self):
        nums = [1,5,2]
        Output= False
        self.assertEqual(Output, get_sol().predictTheWinner(nums))
    def test02(self):
        nums = [1,5,233,7]
        Output= True
        self.assertEqual(Output, get_sol().predictTheWinner(nums))
    def test03(self):
        nums = [1,2,99]
        Output= True
        self.assertEqual(Output, get_sol().predictTheWinner(nums))
    def test04(self):
        nums = [1000,1000,1000,0,0,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
        Output= True
        self.assertEqual(Output, get_sol().predictTheWinner(nums))
    def test05(self):
        nums = [1, 5, 3, 8, 2]
        Output= False
        self.assertEqual(Output, get_sol().predictTheWinner(nums))
    def test06(self):
        nums = [0]
        Output= True
        self.assertEqual(Output, get_sol().predictTheWinner(nums))