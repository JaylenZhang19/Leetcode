class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        ans = 0
        start = 0
        current = 0
        for end in range(n):
            current += costs[end]
            while current > maxCost:
                current -= costs[start]
                start += 1
            ans = max(ans, end - start + 1)
        return ans

