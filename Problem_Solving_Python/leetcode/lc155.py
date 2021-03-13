import unittest


class MinStack:

    def __init__(self):
        self.st = [(float('inf'),float('inf'))]
    def __repr__(self):
        return str(self.st)

    def push(self, x: int) -> None:
        value, minn = self.st[-1]
        if x<minn:
            self.st.append((x,x))
        else:
            self.st.append((x,minn))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        value,minn=self.st[-1]
        return value

    def getMin(self) -> int:
        value, minn =self.st[-1]
        return minn

class MyTestCase(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = [None]*len(inputs)
        st = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MinStack':
                st = MinStack()
            elif cmd=='push':
                st.push(input[0])
            elif cmd=='getMin':
                outputs[i] = st.getMin()
            elif cmd=='pop':
                st.pop()
            elif cmd=='top':
                outputs[i] = st.top()
        return outputs
    def test_1(self):
        commands = ["MinStack","push","push","push","getMin","top","pop","getMin"]
        inputs = [[],[-2],[0],[-1],[],[],[],[]]
        outputs = self.do_test(commands, inputs)
        expected = [None,None,None,None,-2,-1,None,-2]
        self.assertEqual(expected,outputs)
    def test_2(self):
        commands = ["MinStack","push","push","push","getMin","pop","top","getMin"]
        inputs = [[],[-2],[0],[-3],[],[],[],[]]
        outputs = self.do_test(commands, inputs)
        expected = [None,None,None,None,-3,None,0,-2]
        self.assertEqual(expected,outputs)
