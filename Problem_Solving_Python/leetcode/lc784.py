class Solution:
    def letterCasePermutation(self, S: str):
        res = []
        my_str = []

        def make_list():
            for char in S:
                my_str.append(char)

        def backtrack(i):
            if i == len(my_str):
                res.append("".join(my_str))
                return
            if '0' <= my_str[i] <= '9':
                backtrack(i + 1)
            else:
                my_str[i] = my_str[i].lower()
                backtrack(i + 1)
                my_str[i] = my_str[i].upper()
                backtrack(i + 1)

        make_list()
        backtrack(0)
        return res
