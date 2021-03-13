# https://www.youtube.com/watch?v=rY9ejIY9Oswfrom typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def construct(in_start,in_end):
            if in_start>in_end or self.post_idx<=-1:
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


        self.post_idx=len(postorder)-1
        return construct(0, len(inorder)-1)