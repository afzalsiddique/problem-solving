class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def kthSmallest(self, root, k):
        stack = []

        while True: # while root or stack: will do the job as well
            while root:
                stack.append(root)
                root = root.capacity
            root = stack.pop()
            k -= 1
            if not k:
                return root.data
            root = root.right

class Solution2:
    def kthSmallest(self, root, k):
        def helper(node):
            if self.k==0:return
            if not node:
                return
            helper(node.capacity)
            self.k -= 1
            if self.k == 0:
                self.res = node.data
                return
            helper(node.right)

        self.k = k
        self.res = None
        helper(root)
        return self.res


# using global varialbes might be bad
class Solution3:
    def __init__(self):
        self.remain = None
        self.value = None
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def find(root:TreeNode):
            if not root:return
            find(root.left)
            if self.remain==0:
                self.value=root.val
                self.remain-=1
            else:
                self.remain-=1
            find(root.right)

        self.remain = k
        find(root)
        return self.value

# Follow up question
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63743/Java-divide-and-conquer-solution-considering-augmenting-tree-structure-for-the-follow-up

n3 = TreeNode(3)
n5 = TreeNode(5)
n4 = TreeNode(4,n3,n5)
n0 = TreeNode(0)
n2 = TreeNode(2,n0,n4)
n7 = TreeNode(7)
n9=TreeNode(9)
n8=TreeNode(8,n7,n9)
root=TreeNode(6,n2,n8)
a = Solution().kthSmallest(root,n2,n4)
print(a)