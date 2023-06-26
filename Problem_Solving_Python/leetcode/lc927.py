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
class Solution3:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def findIdxOfLastOneInEachPart():
            oneCounts={1,k+1,2*k+1}
            li=[]
            i=n-1
            cnt=0
            while i>=0:
                if arr[i]==1:
                    cnt+=1
                if cnt in oneCounts:
                    li.append(i)
                    oneCounts.remove(cnt)
                i-=1
            return li
        def getNoOfZerosAtEnd(): # for right most part
            i=n-1
            zeros=0
            while i>=0 and arr[i]==0:
                zeros+=1
                i-=1
            return zeros
        def enoughZerosAtEnd(middle_idx, left_idx, noOfZerosAtEnd): # for left part and middle part
            zeroCount=0
            while middle_idx<n and left_idx<n and zeroCount!=noOfZerosAtEnd:
                if arr[middle_idx]!=0 or arr[left_idx]!=0:
                    return False
                middle_idx+=1
                left_idx+=1
                zeroCount+=1
            return zeroCount == noOfZerosAtEnd


        n=len(arr)
        noOfOnes=sum(arr)
        if noOfOnes==0: return [0,2]
        if noOfOnes%3!=0: return [-1,-1]
        k=noOfOnes//3
        right_idx,middle_idx,left_idx=findIdxOfLastOneInEachPart()
        r_i,m_i,l_i=right_idx,middle_idx,left_idx # keeping a copy
        noOfZerosAtEnd=getNoOfZerosAtEnd()
        if not enoughZerosAtEnd(middle_idx+1,left_idx+1,noOfZerosAtEnd):
            return [-1,-1]

        cntOnes=0
        while cntOnes<k:
            if not arr[left_idx]==arr[middle_idx]==arr[right_idx]:
                return [-1,-1]
            if arr[left_idx]==1:
                cntOnes+=1
            left_idx-=1
            middle_idx-=1
            right_idx-=1
        return [l_i+noOfZerosAtEnd,m_i+noOfZerosAtEnd+1]
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
        self.assertEqual([181,340], get_sol().threeEqualParts([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    def test5(self):
        self.assertEqual([0,2], get_sol().threeEqualParts([0,0,0,0,0]))
    def test6(self):
        self.assertEqual([0,2], get_sol().threeEqualParts([0,0,0]))
    def test7(self):
        self.assertEqual([-1,-1], get_sol().threeEqualParts([1,1,0,0,1,0]))
    def test8(self):
        self.assertEqual([2,6], get_sol().threeEqualParts([1,0,0
                                                          ,1,0,0,
                                                       0,0,1,0,0]))
    def test9(self):
        self.assertEqual([15,32], get_sol().threeEqualParts([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0
                                                            ,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,
                                                         0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]))
