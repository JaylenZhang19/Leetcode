
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        
        def build_graph(root, par):
            if root:
                if root.left:
                    graph[root.val].append(root.left.val)
                    graph[root.left.val].append(root.val)
                    build_graph(root.left, root)
                if root.right:
                    graph[root.val].append(root.right.val)
                    graph[root.right.val].append(root.val)
                    build_graph(root.right, root)
        build_graph(root, None)
        
        queue = [k]
        v = set()
        while queue:
            current = queue.pop(0)
            if len(graph[current]) == 0:
                return current
            if len(graph[current]) == 1 and current != root.val:
                return current
            for nei in graph[current]:
                if nei and nei not in v:
                    v.add(nei)
                    queue.append(nei)
    
        
                
            
    
        