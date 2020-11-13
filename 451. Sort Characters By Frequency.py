class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        ret = sorted(sorted(s), key=lambda x: count[x], reverse=True)
        return "".join(ret)