class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        memo = collections.defaultdict(int)
        ret = []
        for name in names:
            if name in memo:
                num = memo[name]
                while f"{name}({num})" in memo:
                    num += 1
                ret.append(f"{name}({num})")
                memo[f"{name}({num})"] = 1
                memo[name] = num + 1
            else:
                ret.append(name)
                memo[name] = 1
        return ret