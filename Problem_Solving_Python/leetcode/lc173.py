import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        self.put_left(root)
    def put_left(self, root:TreeNode):
        if not root:return
        self.st.append(root)
        self.put_left(root.left)

    # iterative
    # def put_left(self,root:TreeNode):
    #     while root:
    #         self.st.append(root)
    #         root = root.left

    def next(self) -> int:
        nxt = self.st.pop()
        self.put_left(nxt.right)
        return nxt.val

    def hasNext(self) -> bool:
        if self.st:return True
        return False



def deserialize(data):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<1:return None
    root = TreeNode(int(data[0]))
    q = deque()
    q.append(root)
    i=1
    while i<l and q:

        curr = q.popleft()
        if data[i]!=en:
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='BSTIterator':
                obj = BSTIterator(deserialize(input[0]))
                outputs.append(None)
            elif cmd=='next':
                outputs.append(obj.next())
            elif cmd=='hasNext':
                outputs.append(obj.hasNext())
        return outputs
    def test_1(self):
        commands = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
        inputs=[['7,3,15,null,null,9,20'], [], [], [], [], [], [], [], [], []]
        out_exptected = [None, 3, 7, True, 9, True, 15, True, 20, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
