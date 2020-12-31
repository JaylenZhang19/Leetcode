class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        
        step = 0
        current = 0
        while current < target:
            step += 1
            current += step
            
        return step if (current - target) % 2 == 0 else step + 1 + step % 2
        