import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()


class Solution:
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
    def test_01(self):
        pushed = [1,2,3,4,5]
        popped = [4,3,5,2,1]
        Output= True
        self.assertEqual(Output, get_sol_obj().validateStackSequences(pushed, popped))
    def test_02(self):
        pushed = [1,2,3,4,5]
        popped = [4,3,5,1,2]
        Output= False
        self.assertEqual(Output, get_sol_obj().validateStackSequences(pushed, popped))