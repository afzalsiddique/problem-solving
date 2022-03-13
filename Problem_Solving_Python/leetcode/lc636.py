import unittest
from collections import deque, defaultdict
from typing import List
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/exclusive-time-of-functions/discuss/153497/Java-solution-using-stack-wrapper-class-and-calculation-when-pop-element-from-the-stack.
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        st = []
        # for log in logs:
        #     i, typ, time = log.split(':')
        for i,typ,time in [log.split(':') for log in logs]:
            i,time=int(i),int(time)
            i, time = int(i), int(time)
            if typ == 'start':
                st.append((i,time))
            else:
                _,start = st.pop()
                running_time = time-start+1
                ans[i]+=running_time
                if st:
                    # subtract running time in advance
                    ans[st[-1][0]]-=running_time
        return ans
class Solution2:
    # https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation
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

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([3,4], get_sol().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    def test02(self):
        self.assertEqual([8], get_sol().exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    def test03(self):
        self.assertEqual([7,1], get_sol().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
    def test04(self):
        self.assertEqual([8,1], get_sol().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]))
    def test05(self):
        self.assertEqual([1], get_sol().exclusiveTime(1, ["0:start:0","0:end:0"]))
