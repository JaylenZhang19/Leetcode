class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        def last_index(row):
            for i in range(len(row) - 1, -1, -1):
                if row[i] == 1:
                    return i
            return -1
        last = [last_index(r) for r in grid]
        n = len(last)
        ret = 0
        for i in range(n):
            j = i
            while j < n and last[j] > i:
                j += 1
            if j == n:
                return -1
            else:
                ret += (j - i)
                last[i + 1 : j + 1] = last[i : j]
                
        return ret