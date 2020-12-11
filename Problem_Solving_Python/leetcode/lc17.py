# https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution/10980
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        def helper(li, mystr, digits):
            i = len(mystr)
            if len(mystr) == len(digits):
                li.append(mystr)
                return

            if digits[i] == '2':
                helper(li, mystr + "a", digits)
                helper(li, mystr + "b", digits)
                helper(li, mystr + "c", digits)

            if digits[i] == '3':
                helper(li, mystr + "d", digits)
                helper(li, mystr + "e", digits)
                helper(li, mystr + "f", digits)

            if digits[i] == '4':
                helper(li, mystr + "g", digits)
                helper(li, mystr + "h", digits)
                helper(li, mystr + "i", digits)

            if digits[i] == '5':
                helper(li, mystr + "j", digits)
                helper(li, mystr + "k", digits)
                helper(li, mystr + "l", digits)

            if digits[i] == '6':
                helper(li, mystr + "m", digits)
                helper(li, mystr + "n", digits)
                helper(li, mystr + "o", digits)

            if digits[i] == '7':
                helper(li, mystr + "p", digits)
                helper(li, mystr + "q", digits)
                helper(li, mystr + "r", digits)
                helper(li, mystr + "s", digits)

            if digits[i] == '8':
                helper(li, mystr + "t", digits)
                helper(li, mystr + "u", digits)
                helper(li, mystr + "v", digits)

            if digits[i] == '9':
                helper(li, mystr + "w", digits)
                helper(li, mystr + "x", digits)
                helper(li, mystr + "y", digits)
                helper(li, mystr + "z", digits)

        li = []
        helper(li, "", digits)
        return li