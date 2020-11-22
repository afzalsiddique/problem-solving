from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.helper(input)

    def helper(self, str):
        li = []
        for i in range(len(str)):
            if str[i] == '*' or str[i] == '-' or str[i] == '+':
                left = self.helper(str[:i])
                right = self.helper(str[i + 1:])
                for item_left in left:
                    for item_right in right:
                        if str[i] == '*':
                            li.append(int(item_left) * int(item_right))
                        elif str[i] == '+':
                            li.append(int(item_left) + int(item_right))
                        else:
                            li.append(int(item_left) - int(item_right))
        if len(li) == 0:
            return [int(str)]

        return li
