class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if len(input) == 0:
            return []
        res = re.split('(\+|-|\*)', input)

        n = len(res)
        dp = collections.defaultdict(list)

        def helper(l, h):
            if l == h:
                return [int(res[l])]
            if (l, h) in dp:
                return dp[(l, h)]
            ret = []
            for s_index in range(l + 1, h, 2):
                left = helper(l, s_index - 1)
                right = helper(s_index + 1, h)
                if res[s_index] == '+':
                    ret += [le + ri for le in left for ri in right]
                elif res[s_index] == '-':
                    ret += [le - ri for le in left for ri in right]
                elif res[s_index] == '*':
                    ret += [le * ri for le in left for ri in right]
            dp[(l, h)] = ret
            return ret
        return helper(0, n-1)