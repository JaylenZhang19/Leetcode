
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[y] = find(x)
        par = {}
        ans = None
        for start, end in edges:
            if end in par:
                ans = [start, end]
                continue
            if find(start) == find(end) and not ans:
                ans = [start, end]
            union(start, end)
            par[end] = start
        return ans if len(set(map(find, range(1, n + 1))))==1 else (par[ans[1]], ans[1])
           
        