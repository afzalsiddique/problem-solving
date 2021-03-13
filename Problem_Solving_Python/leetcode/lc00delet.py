from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        k = 'NOTFOUND'
        i=n-1
        while i>0:
            if nums[i-1]<nums[i]:
                k=i-1
                break
        if k=='NOTFOUND':
            nums.reverse()
            return
        i=n-1
        while True:
            if nums[i]>nums[k]:
                nums[i],nums[k]=nums[k],nums[i]
                break
        lo=k+1
        hi=n-1
        while lo<=hi:
            nums[lo],nums[hi]=nums[hi],nums[lo]
            lo+=1
            hi-=1

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.combinationSum([2,3,6,7], 7))
        expected = sorted([[2,2,3],[7]])
        self.assertEqual(expected, actual)