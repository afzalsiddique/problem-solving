import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# class Solution0:
    # try doing it wihtout hashmap later. check out the solution link below.
    # https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss/685470/Python-One-pass-prefix-sum-O(n)/580146
    # def minSumOfLengths(self, arr: List[int], target: int) -> int:

class Solution:
    # https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss/685486/JAVA-O(N)-Time-Two-Pass-Solution-using-HashMap.
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        first,res=float('inf'),float('inf')
        flag=False # ensures at least two sub array exist
        di={0:-1}
        cur=0
        for i in range(n):
            cur+=arr[i]
            di[cur]=i

        cur=0
        for i in range(n):
            cur+=arr[i]
            if (cur-target) in di: # look behind
                first=min(first,i-di[cur-target])
                flag=True
            if (cur+target) in di and flag: # look forward
                res = min(res,di[cur+target]-i+first) # updates the result only if both left and right sub-array exists. ensures non-overlapping property

        return res if res!=float('inf') else -1
class Solution2:
    # wrong
    # https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss/685486/JAVA-O(N)-Time-Two-Pass-Solution-using-HashMap.
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        first,second=float('inf'),float('inf')
        flag=False
        di={0:-1}
        cur=0
        for i in range(n):
            cur+=arr[i]
            di[cur]=i

        cur=0
        for i in range(n):
            cur+=arr[i]
            if (cur-target) in di: # look behind
                first=min(first,i-di[cur-target])
                flag=True
            if (cur+target) in di and flag: # look forward
                second =min(second,di[cur+target]-i) # non-overlapping property is not ensured

        res=first+second
        if res!=float('inf'): return res
        return -1
class Solution3:
    # wrong
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        pre = list(itertools.accumulate(arr,operator.add))
        l,r=0,0
        res=[]
        while r<n:
            tmp=pre[r]-pre[l]+arr[l]
            if tmp>target:
                if l<r:
                    l+=1
                else:
                    l+=1
                    r+=1
            elif tmp<target:
                r+=1
            else:
                res.append(r-l+1) # append window length
                r+=1 # get out of this window
                l=r
        print(res)
        if len(res)<2:
            return -1

        # find two smallest window
        minn1,minn2=float('inf'),float('inf')
        minn1_idx=0
        for i in range(len(res)):
            if res[i]<minn1:
                minn1=res[i]
                minn1_idx=i
        for i in range(len(res)):
            if res[i]<=minn2 and i!=minn1_idx:
                minn2=res[i]
        return minn1+minn2

class tester(unittest.TestCase):
    def test_1(self):
        arr = [5,5,4,4,5]
        target = 3
        Output= -1
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_2(self):
        arr = [4,3,2,6,2,3,4]
        target = 6
        Output= -1
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_3(self):
        arr = [7,3,4,7]
        target = 7
        Output= 2
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_4(self):
        arr = [3,2,2,4,3]
        target = 3
        Output= 2
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_5(self):
        arr = [3,1,1,1,5,1,2,1]
        target = 3
        Output= 3
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_6(self):
        arr = [1,6,1]
        target = 7
        Output= -1
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_7(self):
        arr = [2,1,3,3,2,3,1]
        target = 6
        Output= 5
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
    def test_8(self):
        arr = [1,1,1,2,2,2,4,4]
        target = 6
        Output= 6
        self.assertEqual(Output, get_sol().minSumOfLengths(arr,target))
