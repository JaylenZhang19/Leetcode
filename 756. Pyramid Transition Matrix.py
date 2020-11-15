class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        def helper(layer):
            if len(layer) == 1:
                return True
            return any(helper(next_layer) for next_layer in builder(layer, 0))

        def builder(l, index):
            if index == len(l) - 2:
                return [c[2] for c in allowed if l[index:index + 2] == c[:2]]
            comb = builder(l, index + 1)
            if not comb:
                return []
            else:
                new_comb = []
                cans = [c[2] for c in allowed if l[index:index + 2] == c[:2]]
                for c in cans:
                    for com in comb:
                        new_comb.append(c + com)
                return new_comb

        return helper(bottom)


