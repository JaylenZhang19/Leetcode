class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full_mask = (1 << n) - 1
        queue = []
        levels = 0
        visited = set()
        for i in range(n):
            queue.append((i, (1 << i)))
            visited.add((i, (1 << i)))
        while queue:
            size = len(queue)
            for _ in range(size):
                node, current_mask = queue.pop(0)
                if current_mask == full_mask:
                    return levels
                for nei in graph[node]:
                    if (nei, (current_mask | (1 << nei))) not in visited:
                        queue.append((nei, (current_mask | (1 << nei))))
                        visited.add((nei, (current_mask | (1 << nei))))
            levels += 1