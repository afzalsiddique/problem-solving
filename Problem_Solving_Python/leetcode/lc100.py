from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right =None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

# iterative
class Solution:
    def isSameTree(self, p, q):
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.value != q.value:
                return False
            return True

        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

# recursive1
class Solution2:
    def isSameTree(self, p, q):
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.value != q.value:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


# my code. pretty ugly:(
class Solution3:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and not q:return False
        if not p and q:return False
        if not p and not q:return True
        q1,q2=deque([p]),deque([q])

        while q1 and q2:
            node1,node2 = q1.popleft(), q2.popleft()
            if node1.val != node2.val: return False
            if len(q1) != len(q2): return False
            if node1.left and not node2.left:return False
            if not node1.left and node2.left:return False
            if node1.right and not node2.right:return False
            if not node1.right and node2.right:return False
            if node1.left:
                q1.append(node1.left)
            if node1.right:
                q1.append(node1.right)
            if node2.left:
                q2.append(node2.left)
            if node2.right:
                q2.append(node2.right)
        if not q1 and not q2:
            return True
        return False