class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 1
        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            space = (i - 1) * 2 + 1
            val = (space + 1) * space // 2
            ans = (val * ans) % mod
        return ans