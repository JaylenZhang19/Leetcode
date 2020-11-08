class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0
        memo = collections.defaultdict(int)
        memo[s[0]] += 1
        ans = 0
        for i in range(1, n):
            memo[s[i]] += 1
            while len(memo.keys()) == 3:
                memo[s[left]] -= 1
                if memo[s[left]] == 0:
                    del memo[s[left]]
                left += 1
                ans += (n - i)
        return ans          