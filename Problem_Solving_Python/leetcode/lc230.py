class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def __init__(self):
        self.cnt = None
        self.value = None
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def find(root:TreeNode):
            if not root:return
            find(root.left)
            if self.cnt==0:
                self.value=root.val
                self.cnt-=1
            else:
                self.cnt-=1
            find(root.right)

        self.cnt = k
        find(root)
        return self.value



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