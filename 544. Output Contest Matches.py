class Solution:
    def findContestMatch(self, n: int) -> str:
        queue = [str(i) for i in range(1, n+1)]
        
        while len(queue) > 1:
            next_queue = []
            while queue:
                first = queue.pop(0)
                last = queue.pop()
                next_queue.append('('+first+','+last+')')
            queue = next_queue
        return queue[0]