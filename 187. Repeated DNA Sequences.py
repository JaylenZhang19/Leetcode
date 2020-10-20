class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 11:
            return []
        c2i = {'A':1, "C":2, "G":3, "T":4}
        nums = [c2i[s[i]] for i in range(n)]
        a = 4
        al = 4 ** 10
        rk = 0
        for i in range(10):
            rk = rk * a + nums[i]
        seen = set()
        seen.add(rk)
        ret = []
        for i in range(10, n):
            rk = (rk * a) - (nums[i-10] * al) + nums[i]
            if rk in seen and s[i-9:i+1] not in ret:
                ret.append(s[i-9:i+1])
            seen.add(rk)
        return ret