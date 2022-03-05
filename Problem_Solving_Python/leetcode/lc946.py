from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n=len(pushed)
        st=[]
        i,j=0,0
        while i<n:
            while j<n and st and st[-1]==popped[j]:
                st.pop()
                j+=1
            st.append(pushed[i])
            i+=1
        while j<n and st and st[-1]==popped[j]:
            st.pop()
            j+=1
        return j==n
class Solution3:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n=len(pushed)
        st=[]
        i,j=0,0
        while i<n:
            if j<n and st and st[-1]==popped[j]:
                st.pop()
                j+=1
            else:
                st.append(pushed[i])
                i+=1
        while j<n and st and st[-1]==popped[j]:
            st.pop()
            j+=1
        return j==n
class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        pushed = deque(pushed)
        popped = deque(popped)
        while pushed:
            if not st:
                st.append(pushed.popleft())
            else:
                if st[-1]==popped[0]:
                    st.pop()
                    popped.popleft()
                else:
                    st.append(pushed.popleft())
        while st and popped and st[-1]==popped[0]:
            st.pop()
            popped.popleft()
        if not st and not popped: return True
        return False


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().validateStackSequences([1,2,3,4,5], [4,3,5,2,1]))
    def test02(self):
        self.assertEqual(False, get_sol().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))