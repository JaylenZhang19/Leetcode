class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        ret = float('-inf')
        for win_size in range(minSize, maxSize+1):
            seen = collections.defaultdict(int)
            for start in range(n - win_size+1):
                if len(set(s[start:start+win_size])) <= maxLetters:
                    seen[s[start:start+win_size]] += 1
                    ret = max(ret, seen[s[start:start+win_size]])
        return ret if ret != float('-inf') else 0