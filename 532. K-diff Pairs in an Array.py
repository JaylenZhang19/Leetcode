class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        seen_word = set()
        for n in nums:
            if n - k in seen_word:
                seen.add((n-k, n))
            if n + k in seen_word:
                seen.add((n, n + k))
            seen_word.add(n)
        return len(seen)