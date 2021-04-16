# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37715/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return None
        dq = deque([root])
        while dq:
            curr = dq.popleft()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next=curr.next.left
                dq.append(curr.left)
                dq.append(curr.right)
        return root
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return None
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.right and cur.left:
                cur.left.next = cur.right
                q.append(cur.left)
                q.append(cur.right)
            if cur.right and cur.next:
                cur.right.next=cur.next.left if cur.next.left else cur.next.right
        return root
