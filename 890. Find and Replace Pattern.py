class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        for word in words:
            match1 = {}
            match2 = {}
            for i in range(len(word)):
                c1 = word[i]
                c2 = pattern[i]
                match1[c2] = c1
                match2[c1] = c2
            ans1 = [match1[c] for c in pattern]
            ans2 = [match2[c] for c in word]
            if "".join(ans1) == word and "".join(ans2) == pattern:
                ret.append(word)
        return ret