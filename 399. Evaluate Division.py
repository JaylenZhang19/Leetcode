class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = collections.defaultdict(collections.defaultdict)
        for (first, second), val in zip(equations, values):
            path[first][second] = val
            path[second][first] = 1/val

        def helper(current, target):
            if current == target:
                return 1
            visited.add(current)
            neighbors = path[current]
            for nei, weights in neighbors.items():
                if nei not in visited:
                    num = helper(nei, target)
                    if num != -1:
                        visited.remove(current)
                        return weights * num
            visited.remove(current)
            return -1

        ans = []
        for start, end in queries:
            if start not in path or end not in path:
                ans.append(-1)
            elif start == end:
                ans.append(1)
            else:
                visited = set()
                ans.append(helper(start, end))
        return ans