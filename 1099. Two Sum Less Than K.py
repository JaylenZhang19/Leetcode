class Solution:
    def twoSumLessThanK(self, a: List[int], k: int) -> int:
        n = len(a)
        a.sort()
        left = 0
        right = n - 1
        ans = -1
        while left < right:
            if a[right] + a[left] < k:
               
                ans = a[right] + a[left]if k - ans > k - (a[right] + a[left]) else ans
            if a[right] + a[left] > k:
                right -= 1
            else:
                left += 1
        return ans
            
        