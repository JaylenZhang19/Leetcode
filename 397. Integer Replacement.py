class Solution:
    def integerReplacement(self, n: int) -> int:
        queue = [n]

        seen = set()
        seen.add(n)
        times = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.pop(0)
                if current == 1:
                    return times
                if current % 2:
                    if current + 1 not in seen:
                        queue.append(current+1)
                        seen.add(current+1)
                    if current - 1 not in seen:
                        queue.append(current - 1)
                        seen.add(current - 1)
                else:
                    if current // 2 not in seen:
                        queue.append(current // 2)
                        seen.add(current // 2)
            times += 1
    
            