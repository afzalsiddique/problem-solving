# https://www.youtube.com/watch?v=kqHNP6NTzME&t=4m51s
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def helper(node:TreeNode, row:int,col:int):
            if node is None:return

            di[col].append((node.val,row,col))
            helper(node.left, row + 1,col-1)
            helper(node.right, row + 1,col+1)
            return


        di = defaultdict(list)
        helper(root,0,0)
        result = []
        for x in sorted(di.keys()):
            temp = sorted(di[x],key=lambda x:(x[2],x[1],x[0]))# sort based on col,row and then val
            result.append([item[0] for item in temp])

        return result
