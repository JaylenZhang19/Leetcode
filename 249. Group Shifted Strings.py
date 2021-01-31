class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        pattern = collections.defaultdict(list)
        for word in strings:
            p = []
            w = word[0]
            for c in word:
                p.append((ord(c) - ord(w) + 26) % 26) 
            pattern[tuple(p)].append(word)
        ans = []
        for k in pattern.keys():
            ans.append(pattern[k])
        return ans