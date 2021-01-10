class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        ret = []
        queue = []
        for b in B:
            if A:
                queue.append(A.pop(0))
            index = bisect.bisect_right(queue, b)
            while index == len(queue)  and A:
                queue.append(A.pop(0))
                index = bisect.bisect_right(queue, b)
            if index == len(queue):
                ret.append(queue.pop(0))
            else:
                ret.append(queue.pop(index))
        return ret