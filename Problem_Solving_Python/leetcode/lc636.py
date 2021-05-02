import unittest
from collections import deque, defaultdict
from typing import List

# https://leetcode.com/problems/exclusive-time-of-functions/discuss/153497/Java-solution-using-stack-wrapper-class-and-calculation-when-pop-element-from-the-stack.
class Solution:
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        st = []
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == 'start':
                st.append((fn,time))
            else:
                _,start = st.pop()
                running_time = time-start+1
                ans[fn]+=running_time
                if st:
                    # subtract running time in advance
                    ans[st[-1][0]]-=running_time
        return ans
# https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation
class Solution2:
    def exclusiveTime(self, N, logs):
        ans = [0] * N
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans

def get_sol_obj(): return Solution()
class tester(unittest.TestCase):
    def test1(self):
        n = 2
        logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        Output= [3,4]
        self.assertEqual(Output,get_sol_obj().exclusiveTime(n, logs))
    def test2(self):
        n = 1
        logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
        Output= [8]
        self.assertEqual(Output,get_sol_obj().exclusiveTime(n, logs))
    def test3(self):
        n = 2
        logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
        Output= [7,1]
        self.assertEqual(Output,get_sol_obj().exclusiveTime(n, logs))
    def test4(self):
        n = 2
        logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
        Output= [8,1]
        self.assertEqual(Output,get_sol_obj().exclusiveTime(n, logs))
    def test5(self):
        n = 1
        logs = ["0:start:0","0:end:0"]
        Output= [1]
        self.assertEqual(Output,get_sol_obj().exclusiveTime(n, logs))
