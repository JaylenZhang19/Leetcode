class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(set)
        ans = [-1] * n
        for par, child in edges:
            graph[par].add(child)
            graph[child].add(par)

        def helper(node, parent):
            current_count = collections.defaultdict(int)
            current_count[labels[node]] += 1
            if len(graph[node]) == 1 and list(graph[node])[0] == parent:
                ans[node] = current_count[labels[node]]
                return current_count
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_count = helper(nei, node)
                for k in child_count.keys():
                    if k in current_count:
                        current_count[k] += child_count[k]
                    else:
                        current_count[k] = child_count[k]
            ans[node] = current_count[labels[node]]
            return current_count
        helper(0, -1)
        return ans