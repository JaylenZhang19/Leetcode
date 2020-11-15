class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        n = len(arr)
        s = 0
        start = 0
        ans = float('inf')
        bestSoFar = float('inf')
        best = [float('inf')] * n
        for end in range(n):
            s += arr[end]
            while s > target:
                s -= arr[start]
                start += 1
            if s == target:
                if start > 0 and best[start-1] != float('inf'):
                    ans = min(ans, best[start-1] + end - start + 1)
                bestSoFar = min(bestSoFar, end - start + 1)
            best[end] = bestSoFar
        return -1 if ans == float('inf') else ans

