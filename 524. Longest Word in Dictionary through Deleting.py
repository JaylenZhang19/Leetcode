class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        memo = collections.defaultdict(list)
        for i, c in enumerate(s):
            memo[c].append(i)
        d.sort()
        for word in sorted(d, key = lambda x: len(x), reverse=True):
            position = 0;
            for c in word:
                if c not in memo:
                    break
                candi = [i for i in memo[c] if i >= position]
                if not candi:
                    break
                else:
                    position = candi[0] + 1
            else:
                return word
        return ""
                