class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def helper():
            n1 = len(str1)
            n2 = len(str2)
            dp = [["" for _ in range(n2)] for _ in range(n1)]
            for i in range(n1):
                for j in range(n2):
                    if str1[i] == str2[j]:
                        dp[i][j] = str1[i] if (i - 1 < 0 or j - 1 < 0) else dp[i-1][j-1] + str1[i]  
                    else:
                        ans1 = dp[i-1][j] if i - 1 >= 0 else ""
                        ans2 = dp[i][j - 1] if j - 1 >= 0 else ""
                        dp[i][j] = ans1 if len(ans1) > len(ans2) else ans2
            return dp[-1][-1]
        
        lcs = helper()
        i = j = 0
        ret = ""
        for c in lcs:
            while str1[i] != c:
                ret += str1[i]
                i += 1
            while str2[j] != c:
                ret += str2[j]
                j += 1
            ret += c
            i += 1
            j += 1
        return ret + str1[i:] + str2[j:]
            