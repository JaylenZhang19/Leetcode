class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        seen = {val:i for i, val in enumerate(target)}
        queue = []
        ret = 0
        for num in arr:
            if num not in seen:
                continue
            index = bisect.bisect_left(queue, seen[num])
            if index == len(queue):
                queue.append(seen[num])
            else:
                queue[index] = seen[num]
            ret = max(ret, len(queue))
        return len(target) - ret
            