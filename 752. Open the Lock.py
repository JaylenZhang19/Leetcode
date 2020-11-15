class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        seen.add('0000')
        
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        
        queue = ['0000']
        length = 0
        while queue:
            
            for _ in range(len(queue)):
                current = queue.pop(0)
                if current == target:
                    return length
                if current in deadends:
                    continue
                for nei in neighbors(current):
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            length += 1
        return -1
                        
                        
                    