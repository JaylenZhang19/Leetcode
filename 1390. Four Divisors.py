class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            last_d = 0
            d = 2
            while d * d <= n:
                if n % d == 0:
                    if last_d == 0:
                        last_d = d
                    else:
                        last_d = 0
                        break
                d += 1
            if last_d > 0 and last_d != (n // last_d):
                s = s + 1 + n + last_d + (n // last_d)
        return s
            