class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        first = 1 if s[0] == '1' else 0
        ret = first
        for i in range(1, n):
            second = 0
            if s[i] == '1':
                second = first + 1
                ret += second
            first = second
        return ret % (10 ** 9 + 7)