class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        
        def helper(node, par):
            dis = 0
           
            for nei in graph[node]:
                if nei != par:
                    child_dis = helper(nei, node)
                    dis += child_dis
            if hasApple[node]:
                return dis + 2
            elif dis != 0:
                return dis + 2
            else:
                return 0
        ans = helper(0, -1)
        return ans - 2 if ans else 0