class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo = {}
        def helper(time, state):
            if time >= n:
                return 1
            if (time, state) in memo:
                return memo[(time, state)]
            count = 0
            for i in range(6):
                choose = (state >> (i * 4)) & 15
                if choose < rollMax[i]:
                    count += helper(time + 1, (choose + 1) << (i * 4))
                    count = count % (10 ** 9 + 7)
            memo[(time, state)] = count
            return memo[(time, state)]
        return helper(0, 0)