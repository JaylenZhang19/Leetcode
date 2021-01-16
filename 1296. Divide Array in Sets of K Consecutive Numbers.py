class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        for i in sorted(c):
            if c[i] > 0:
                val = c[i]
                for j in range(k):
                    c[i + j] -= val
                    if c[i + j] < 0:
                        return False
        return True
        
            
            
            
                