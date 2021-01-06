class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = (10 ** 9) + 7
        can = set([2 ** i for i in range(0, 22)])
        ret = 0
        seen = collections.defaultdict(int)
        for val in deliciousness:
            for s in can:
                if s - val in seen:
                    ret = (ret + seen[s - val]) % mod
            seen[val] += 1
        return ret
            
                