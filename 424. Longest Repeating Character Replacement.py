class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        left = 0
        ans = 0
        for index, val in enumerate(s):
            count[val] += 1
            while len(count.keys()) > k + 1:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            while sum([v for v in sorted(count.values(), reverse=True)[1:]]) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans = max(ans, index - left + 1)
        return ans