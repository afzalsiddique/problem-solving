import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        dp=[[None]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=nums1[i]*nums2[j]
                elif i==0:
                    dp[i][j]=max(dp[i][j-1],nums1[i]*nums2[j])
                elif j==0:
                    dp[i][j]=max(dp[i-1][j],nums1[i]*nums2[j])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+nums1[i]*nums2[j],nums1[i]*nums2[j])
        return dp[-1][-1]

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(18,get_sol().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))
    def test02(self):
        self.assertEqual(21,get_sol().maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7]))
    def test03(self):
        self.assertEqual(-1,get_sol().maxDotProduct(nums1 = [-1,-1], nums2 = [1,1]))
    def test04(self):
        self.assertEqual(50,get_sol().maxDotProduct([-5,3,-5,-3,1], [-2,4,2,5,-5]))
    def test05(self):
        self.assertEqual(72,get_sol().maxDotProduct([-3,-8,3], [7,-9]))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
