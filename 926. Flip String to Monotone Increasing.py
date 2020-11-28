class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        dp = [0] * n
        for i in reversed(range(n)):
            if i == n - 1:
                dp[i] = 1 if S[i] == '0' else 0
            else: 
                if S[i] == '0':
                    dp[i] = dp[i+1] + 1
                else:
                    dp[i] = dp[i+1]
        ret = float('inf')
        change = 0
        for index, c in enumerate(S):
            ret = min(ret, change + dp[index])
            if c == '1':
                change += 1
        return min(ret, change, dp[0])