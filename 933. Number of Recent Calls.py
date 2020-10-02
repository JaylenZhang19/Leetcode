class RecentCounter:

    def __init__(self):
        self.window = []
        

    def ping(self, t: int) -> int:
        while self.window and self.window[0] < t - 3000:
            self.window.pop(0)
        self.window.append(t)
        return len(self.window)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)