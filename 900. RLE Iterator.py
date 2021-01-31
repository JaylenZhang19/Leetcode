class RLEIterator:

    def __init__(self, A: List[int]):
        self.index = 0
        self.queue = []
        for i in range(1, len(A), 2):
            self.queue.append([A[i - 1], A[i]])
    def next(self, n: int) -> int:
        val = -1
        while self.index < len(self.queue) and n:
            val = self.queue[self.index][1]
            v = min(n, self.queue[self.index][0])
            n -= v
            self.queue[self.index][0] -= v
            if self.queue[self.index][0] == 0:
                self.index += 1
        if n:
            return -1
        else:
            return val


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)