class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            dif = arr[mid] - mid - 1
            if dif >= k:
                right = mid - 1
            else:
                left = mid + 1
        num = arr[left] - left - 1
        d = k - num
        if d <= 0:
            d -= 1

        return arr[left] + d