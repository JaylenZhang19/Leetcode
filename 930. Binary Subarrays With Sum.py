class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        cur_sum = 0
        count = collections.defaultdict(int)
        count[0] = 1
        ans = 0
        for i in range(n):
            cur_sum += A[i]
            ans += count[cur_sum - S]
            count[cur_sum] += 1
        return ans