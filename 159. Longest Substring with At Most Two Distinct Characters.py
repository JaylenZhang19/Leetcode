class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = collections.defaultdict(int)
        start = 0
        ans = 0
        for index, c in enumerate(s):
            dic[c] += 1
            while len(dic) > 2:
                dic[s[start]] -= 1
                if not dic[s[start]]:
                    del dic[s[start]]
                start += 1
            ans = max(ans, index - start + 1)
        return ans