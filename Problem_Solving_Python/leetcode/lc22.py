# https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution/10980
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(li, my_str, no_of_open, no_of_close, n):
            if len(my_str) == 2 * n:
                li.append(my_str)

            if no_of_open < n:
                generate(li, my_str+"(", no_of_open+1, no_of_close, n)

            if no_of_close < no_of_open:
                generate(li, my_str + ")", no_of_open, no_of_close+1, n)

        li = []
        generate(li, "", 0, 0, n)
        return li