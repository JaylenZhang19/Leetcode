class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        if m * k == len(bloomDay):
            return max(bloomDay)
        n = len(bloomDay)
        day = list(set(bloomDay))
        day.sort()
        left = 0
        right = len(day) - 1
        
        def check(day):
            pre = 0
            whole = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    cur = pre + 1
                else:
                    cur = 0
                    whole += pre // k
                pre = cur
                if i == n - 1:
                    whole += pre // k
            return whole >= m
        while left < right:
            mid = left + (right - left) // 2
            if check(day[mid]):
                right = mid
            else:
                left = mid + 1
        return day[left]
        
        
        
        
        
       
        