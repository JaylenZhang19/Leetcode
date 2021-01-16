class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        previous = 0
        current = 1
        while current <= k:
            current, previous = current + previous, current
        if previous == k:
            return 1
        else:
            return 1 + self.findMinFibonacciNumbers(k - previous)
        
    
            