class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for edge in edges:
            if not dsu.union(*edge):
                return edge
            
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)
        
        def bfs(start, end):
            seen = set()
            seen.add(start)
            queue = [start]
            while queue:
                current = queue.pop(0)
                if current == end:
                    return True
                for nei in graph[current]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            return False
        
        for start, end in edges:
            if start in graph and end in graph and bfs(start, end):
                return start, end
            graph[start].append(end)
            graph[end].append(start)
        
        
        
class DSU(object):
    def __init__(self, size):
        self.par = [i for i in range(size+1)]
        self.level = [0] * (size +1)
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.level[px] > self.level[py]:
                self.par[py] = px
            elif self.level[px] < self.level[py]:
                self.par[px] = py
            else:
                self.par[px] = py
                self.level[py] +=1
            return True