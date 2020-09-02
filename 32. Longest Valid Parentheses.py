class Solution:
    # time limit exceeded 
    def longestValidParentheses(self, s: str) -> int:
        maximum = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1):
            j = i + 1
            if s[i] == '(' and s[j] == ')':
                dp[i][j] = True
                maximum = max(maximum, j - i + 1)
        scope = n
        if n % 2 == 1:
            scope = n - 1
        for sc in range(4, scope + 2, 2):
            for start in range(n):
                end = start + sc - 1
                if end < n:
                    if s[start] == '(' and s[end] == ')' and dp[start + 1][end - 1]:
                        dp[start][end] = True
                        maximum = max(maximum, end - start + 1)
                    for m in range(start, end):
                        if dp[start][m - 1] and dp[m][end]:
                            dp[start][end] = True
                            maximum = max(maximum, end - start + 1)
                
        return maximum
        


    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')':
                
                if i-1 >= 0 and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i] >= 0:
                        dp[i] = dp[i] + dp[i - dp[i]]
                if i-1 >= 0 and s[i-1] == '(':
                    if i-2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2 
        return max(dp)