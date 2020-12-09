class Solution:
    def countArrangement(self, N: int) -> int:
        seen = [False] * (N + 1)
        ret = 0

        def helper(index):
            if index == N+1:
                nonlocal ret
                ret += 1
                return
            for i in range(1, N + 1):
                if (i % index == 0 or index % i == 0) and not seen[i]:
                    seen[i] = True
                    helper(index + 1)
                    seen[i] = False

        helper(1)
        return ret