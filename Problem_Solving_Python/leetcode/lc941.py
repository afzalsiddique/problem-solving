import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n<3: return False
        inc=0
        dec=0
        for i in range(1,n):
            if arr[i-1]<arr[i]:
                inc+=1
            else:
                break
        if not inc: return False
        for i in range(i,n):
            if arr[i-1]>arr[i]:
                dec+=1
            else:
                return False
        return inc!=0 and dec!=0


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(False, get_sol().validMountainArray(arr = [2,1]))
    def test02(self):
        self.assertEqual(False, get_sol().validMountainArray(arr = [3,5,5]))
    def test03(self):
        self.assertEqual(True, get_sol().validMountainArray(arr = [0,3,2,1]))
    def test04(self):
        self.assertEqual(False, get_sol().validMountainArray(arr = [0,1,2,1,2]))
    def test05(self):
        self.assertEqual(False, get_sol().validMountainArray(arr = [9,8,7,6,5,4,3,2,1,0]))
    def test06(self):
        self.assertEqual(False, get_sol().validMountainArray(arr = [0,1,2,3,4,5]))
    def test07(self):
        self.assertEqual(False, get_sol().validMountainArray(arr = [4,4,3,2,1]))
    # def test08(self):
    # def test09(self):
