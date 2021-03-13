import heapq


class MaxHeap:
    def __init__(self):
        self.data = []
    def top(self):
        return -self.data[0]
    def push(self, val):
        heapq.heappush(self.data, -val)
    def pop(self):
        return -heapq.heappop(self.data)
    def __repr__(self):
        return str(self.data)
