class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        pre_sum = []
        ret = 0
        for val in arr:
            if pre_sum:
                pre_sum.append(pre_sum[-1] + val)
            else:
                pre_sum.append(val)
        print(pre_sum)
        dp = [0] * n
        for index, val in enumerate(pre_sum):
            if index:
                dp[index] = dp[index-1] + 1 if val % 2 == 1 else dp[index-1]
            else:
                dp[index] = 1 if val % 2 == 1 else 0
        print(dp)
        ret += dp[0]
        for i in range(1, n):
            if pre_sum[i] % 2:
                ret = (ret + 1 + (i - dp[i-1])) % (10 ** 9 + 7)
            else:
                ret = (ret + dp[i-1]) % (10 ** 9 + 7)
                    
        return ret