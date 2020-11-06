class Solution:
    def peopleIndexes(self, favorites: List[List[str]]) -> List[int]:
        record = collections.defaultdict(int)
        n = len(favorites)
        order = list(zip(range(n), favorites))
        order.sort(key=lambda x: len(x[1]), reverse=True)
        is_subset = []
        for index, fav in order:
            res = record[fav[0]]
            for comp in fav[1:]:
                res = res & record[comp]
            if res:
                is_subset.append(index)
            for comp in fav:
                record[comp] = record[comp] | (1 << index)
        return [i for i in range(n) if i not in is_subset]