import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)

        max_left=[-1]*n
        max_left[0]=arr[0]
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],arr[i])

        min_right=[-1]*n
        min_right[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            min_right[i]=min(min_right[i+1],arr[i])

        res=1
        for i in range(n-1):
            if max_left[i]<=min_right[i+1]:
                res+=1
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [5,4,3,2,1]))
    def test02(self):
        self.assertEqual(4, get_sol().maxChunksToSorted(arr = [2,1,3,4,4]))
    def test03(self):
        self.assertEqual(6, get_sol().maxChunksToSorted(arr = [2,1,3,4,4,4,4]))
    def test04(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [4,2,2,3,3]))
    def test05(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,7,6,5]))
    def test06(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,1,7,6,5]))
    def test07(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [1,1,0,0,1]))
    def test08(self):
        self.assertEqual(1, get_sol().maxChunksToSorted(arr = [4,2,2,1,1]))
    def test09(self):
        self.assertEqual(2, get_sol().maxChunksToSorted(arr = [3,2,1,7,6,5,4]))
