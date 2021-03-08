import collections

# using one queue
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1,self.q2=self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if not self.q1:return True
        return False
s=MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
