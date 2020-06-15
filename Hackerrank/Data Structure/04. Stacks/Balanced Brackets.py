#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for x in s:
        if x in ['{', '[', '(']:
            stack.append(x)
        else:
            if not stack:
                return 'NO'
            else:
                top = stack.pop()
                if top=='{' and x!='}':
                    return 'NO'
                elif top=='[' and x!=']':
                    return 'NO'
                elif top=='(' and x!=')':
                    return 'NO'
    if stack:
        return 'NO'
    return 'YES'

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         s = input()

#         result = isBalanced(s)

#         fptr.write(result + '\n')

#     fptr.close()
