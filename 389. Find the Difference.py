class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        for k in c2.keys():
            if c1[k] != c2[k]:
                return k


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        base = 0
        for c in (s + t):
            base ^= ord(c)
        return chr(base)