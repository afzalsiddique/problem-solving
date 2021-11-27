# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        results = []

        def traverse(root:TreeNode):
            if not root:return
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            results.append(root.val)
            return


        traverse(root)
        return results

    # using two stacks
    # https://www.youtube.com/watch?v=qT65HltK2uE&t=127s
    def postorderTraversal__(self, root: TreeNode) -> List[int]:
        if not root:return []
        stack1 = [root]
        stack2 = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr.val)
            if curr.left:
                stack1.append(curr.capacity)
            if curr.right:
                stack1.append(curr.right)

        return stack2[::-1]

    # using one stack
    # https://www.youtube.com/watch?v=Zv14sK2kvtQ
    def postorderTraversal___(self, root: TreeNode) -> List[int]:
        if not root: return []
        st= []
        ans = []
        prev = None # recently popped node

        while root or st:
            # Keep on iterating towards the leftmost node
            while root:
                st.append(root)
                root=root.left

            # If there is no right child
            # or right child is the one that we recently visited
            # it means we have traversed all the nodes of stack[-1]
            if st[-1].right is None or st[-1].right==prev:
                # we will update the prev node
                prev = st.pop()
                ans.append(prev.val)
            else:
                # Otherwise we will visit the right child.
                root = st[-1].right
        return ans
