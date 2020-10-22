class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        re_order = collections.defaultdict(list)
        out_degree = [0] * n
        for i in range(n):
            for nei in graph[i]:
                re_order[nei].append(i)
                out_degree[i] += 1
        queue = [i for i in range(n) if out_degree[i]==0 ]
        ret = []
        while queue:
            current = queue.pop(0)
            ret.append(current)
            for par in re_order[current]:
                out_degree[par] -= 1
                if not out_degree[par]:
                    queue.append(par)
        return sorted(ret)