# https://www.youtube.com/watch?v=rY9ejIY9Oswfrom typing import List
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time: n
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/565412/Detailed-Python-Walkthrough-from-an-O(n2)-solution-to-O(n).-Faster-than-99.77
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.post_idx=len(postorder)-1
        idx ={}
        for i,val in enumerate(inorder):
            idx[val]=i
        def construct(in_start,in_end):
            if in_start>in_end:
                return None

            node = TreeNode(postorder[self.post_idx])
            pos = idx[postorder[self.post_idx]]
            self.post_idx -= 1


            node.right = construct(pos+1, in_end)
            node.left = construct(in_start, pos-1)

            return node


        return construct(0, len(inorder)-1)

class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.post_idx=len(postorder)-1

        def construct(in_start,in_end):
            if in_start>in_end:
                return None

            node = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1

            for i in range(in_start, in_end+1):
                if inorder[i]==node.val:
                    pos=i
                    break

            node.right = construct(pos+1, in_end)
            node.left = construct(in_start, pos-1)

            return node


        return construct(0, len(inorder)-1)

