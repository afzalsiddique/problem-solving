import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/three-equal-parts/discuss/183922/C%2B%2B-O(n)-time-O(1)-space-12-ms-with-explanation-and-comments
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ones = sum(x for x in arr if x==1)
        if ones==0: return [0,len(arr)-1]
        if ones%3!=0: return [-1,-1]
        k=ones//3
        # first one
        cnt=0
        for i in range(n):
            if arr[i]==1:
                cnt+=1
            if cnt==1:
                break
        first=i

        # (k+1)th one
        cnt=0
        for i in range(n):
            if arr[i]==1:
                cnt+=1
            if cnt==k+1:
                break
        mid=i

        # (2*k+1)th one
        cnt=0
        for i in range(n):
            if arr[i]==1:
                cnt+=1
            if cnt==2*k+1:
                break
        last=i

        while last<n and arr[first]==arr[mid]==arr[last]:
            first+=1
            mid+=1
            last+=1
        if last==n:
            return [first-1, mid]
        return [-1,-1]
class Solution2:
    # tle
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n=len(arr)
        for i in range(n):
            tmp1=arr[:i+1]
            val1=int(''.join(map(str,tmp1)))
            for j in range(i+2,n):
                tmp2=arr[i+1:j]
                val2=int(''.join(map(str,tmp2)))
                if val1==val2:
                    tmp3=arr[j:]
                    val3=int(''.join(map(str,tmp3)))
                    if val2==val3:
                        return [i,j]
        return [-1,-1]

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3], get_sol().threeEqualParts([1,0,1,0,1]))
    def test2(self):
        self.assertEqual([-1,-1], get_sol().threeEqualParts([1,1,0,1,1]))
    def test3(self):
        self.assertEqual([0,2], get_sol().threeEqualParts([1,1,0,0,1]))
    def test4(self):
        self.assertEqual([0,2], get_sol().threeEqualParts([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
