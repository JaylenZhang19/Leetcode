class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        
        def make(a):
            ans = [-1] * n
            stack = []
            for i in a:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
        
        larger = make(sorted(range(n), key = lambda i:A[i]))
        smaller = make(sorted(range(n), key = lambda i:-A[i]))

        dp = [[False] * 2 for _ in range(n)]
        dp[-1] = [True, True]
        ret = 1
        for i in range(n-2, -1, -1):
            if smaller[i] != -1:
                dp[i][1] = dp[smaller[i]][0]
            if larger[i] != -1:
                dp[i][0] = dp[larger[i]][1]
                if dp[i][0]:
                    ret += 1
        return ret