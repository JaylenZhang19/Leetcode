class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        
        ans = 0
        for x, y in zip(arr, sorted(arr)):
            count1[x] += 1
            count2[y] += 1
            if count1 == count2:
                ans += 1
                count1.clear()
                count2.clear()
            
        return ans