import re
from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

# without stack
class Solution:
    def calculate(self, s: str) -> int:
        cur, prev, result, sign = 0, 0, 0, '+'
        s += '+'
        for c in s:
            if c == ' ': continue
            if c.isdigit():
                cur = 10 * cur + int(c)
                continue
            if sign == '+':
                result += prev
                prev = cur
            elif sign == '-':
                result += prev
                prev = -cur
            elif sign == '*':
                prev = prev * cur
            elif sign == '/':
                prev = int(prev / cur)
            cur, sign = 0, c
        return result + prev

class Solution2:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        s=s+"+"
        st,prev_sign,num = [],'+',0
        for c in s:
            if c.isdigit():
                num=num*10+ord(c)-ord('0')
            else:
                if prev_sign=='+':
                    st.append(num)
                elif prev_sign=='-':
                    st.append(-num)
                elif prev_sign=='*':
                    st.append(st.pop()*num)
                elif prev_sign=='/':
                    last_num = st.pop()
                    if last_num>0:
                        st.append(last_num//num)
                    else:
                        last_num = -last_num
                        ans = last_num//num
                        st.append(-ans)
                num=0
                prev_sign=c
        return sum(st)


class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(7,Solution().calculate('3+2*2'))
    def test2(self):
        self.assertEqual(13,Solution().calculate("14-3/2"))
    def test3(self):
        self.assertEqual(28,Solution().calculate("2+5+7*3"))
    def test4(self):
        self.assertEqual(17,Solution().calculate("2+5+10"))
    def test5(self):
        self.assertEqual(-14,Solution().calculate("2+5-7*3"))
