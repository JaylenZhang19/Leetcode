class CustomStack:

    def __init__(self, maxSize: int):
        self.maximum = maxSize
        self.current = -1
        self.stack = []
        

    def push(self, x: int) -> None:
        if self.current == self.maximum-1:
            return 
        else:
            self.stack.append(x)
            self.current += 1
        

    def pop(self) -> int:
        if self.current == -1:
            return -1
        else:
            ret = self.stack.pop()
            self.current -= 1
            return ret
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.current+1)):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)