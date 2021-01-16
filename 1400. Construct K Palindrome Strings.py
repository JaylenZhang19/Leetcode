class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = collections.Counter(s)
        odd = sum([1 for val in counter.values() if val % 2])
        return odd <= k and len(s) >= k