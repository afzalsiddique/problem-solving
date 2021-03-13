# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33904/JAVA-Double-Stack-Solution
from typing import List

################################ UNNECESSARY CODES PRESENT IN THIS SOLUTION ##############################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:return []
        st1=[(root,'r')]
        st2=[]
        ans = [[root.val]]

        while st1 or st2:
            sub_ans = []
            while st1:
                node, side = st1.pop()
                if side=='r':
                    if node.right:
                        st2.append((node.right,'l'))
                        sub_ans.append(node.right.val)
                    if node.left:
                        st2.append((node.left,'l'))
                        sub_ans.append(node.left.val)
                else: # side=='l':
                    if node.left:
                        st2.append((node.left,'r'))
                        sub_ans.append(node.left.val)
                    if node.right:
                        st2.append((node.right,'r'))
                        sub_ans.append(node.right.val)
            if sub_ans:
                ans.append(sub_ans)
            sub_ans = []
            while st2:
                node, side = st2.pop()
                if side=='r':
                    if node.right:
                        st1.append((node.right,'l'))
                        sub_ans.append(node.right.val)
                    if node.left:
                        st1.append((node.left,'l'))
                        sub_ans.append(node.left.val)
                else: # side=='l':
                    if node.left:
                        st1.append((node.left,'r'))
                        sub_ans.append(node.left.val)
                    if node.right:
                        st1.append((node.right,'r'))
                        sub_ans.append(node.right.val)
            if sub_ans:
                ans.append(sub_ans)
        return ans
