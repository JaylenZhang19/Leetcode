class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        queue = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    queue.append((i, j))
                if j == i + 1 and s[i] == s[j]:
                    queue.append((i, j))
        ans = [-1, -1]
        longest = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                left, right = queue.pop(0)
                if right - left + 1 > longest:
                    longest = right - left + 1
                    ans = [left, right]
                if left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                    queue.append((left - 1, right + 1))
        return s[ans[0]:ans[1]+1]