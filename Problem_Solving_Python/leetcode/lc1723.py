import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    # same as leetcode 473, 698
    def minimumTimeRequired(self, A: List[int], k: int) -> int:
        def put(index): # dfs
            nonlocal res
            if index==len(A):
                res=min(res,max(buckets))
                return
            seen=set()
            for i in range(len(buckets)):
                if buckets[i] in seen: continue # optimization
                seen.add(buckets[i])
                if buckets[i]+A[index]>res: continue # optimization
                buckets[i]+=A[index]
                put(index+1)
                buckets[i]-=A[index]

        res=float('inf')
        A.sort(reverse=True) # optimization
        buckets=[0]*k
        put(0)
        return res
class Solution2:
    # tle
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrack(i: int):
            if i==n:
                return max(workers)
            res=float('inf')
            for j in range(k):
                workers[j]+=jobs[i]
                res=min(res,backtrack(i + 1))
                workers[j]-=jobs[i]
            return res

        n=len(jobs)
        workers=[0]*k
        return backtrack(0)
class Solution3:
    # tle
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def turnOn(masks:tuple[int],j:int,i:int)->tuple[int]:
            masks=list(masks)
            mask=masks[j]
            mask=mask|(1<<i)
            masks[j]=mask
            return tuple(masks)
        def turnOff(masks:tuple[int],j:int,i:int)->tuple[int]:
            masks=list(masks)
            mask=masks[j]
            mask=mask-(1<<i)
            masks[j]=mask
            return tuple(masks)
        def isOn(mask:int,i:int):
            return mask&(1<<i)
        def getMaxHour(masks:tuple[int]):
            res=float('-inf')
            for mask in masks:
                ans=0
                for i in range(len(jobs)):
                    if isOn(mask,i):
                        ans+=jobs[i]
                res=max(res,ans)
            return res
        @functools.lru_cache(None)
        def backtrack(i: int,masks:tuple[int]):
            if i==n:
                return getMaxHour(masks)
            res=float('inf')
            for j in range(k):
                masks=turnOn(masks,j,i)
                res=min(res,backtrack(i + 1,masks))
                masks=turnOff(masks,j,i)
            return res

        n=len(jobs)
        masks=[0]*k
        return backtrack(0,tuple(masks))


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().minimumTimeRequired([3,2,3], 3))
    def test02(self):
        self.assertEqual(11, get_sol().minimumTimeRequired([1,2,4,7,8], 2))
    def test03(self):
        self.assertEqual(9899456, get_sol().minimumTimeRequired([9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202], 9))
    def test04(self):
        self.assertEqual(504, get_sol().minimumTimeRequired([256,250,255,250,254,255,260,260,250,252,257,253], 9))
    def test05(self):
        self.assertEqual(12, get_sol().minimumTimeRequired([5,5,4,4,4], 2))
    def test06(self):
        self.assertEqual(13, get_sol().minimumTimeRequired([2,3,13], 2))
