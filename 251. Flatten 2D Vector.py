class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.memo = []
        for inner in v:
            for c in inner:
                self.memo.append(c)
        self.n = len(self.memo)
        self.current = 0

    def next(self) -> int:
        if self.current < self.n:
            val = self.memo[self.current]
            self.current += 1
            return val

    def hasNext(self) -> bool:
        return self.current < self.n


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()