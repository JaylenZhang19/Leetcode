class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row = len(mat)
        col = len(mat[0])
        c = [0 for _ in range(row)]
        cur = sum(mat[i][0] for i in range(row))
        if k == 1:
            return cur

        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, [cur, c])
        seen = set()

        for time in range(k):
            val, state = heapq.heappop(heap)
            if time == k-1:
                return val
            for r in range(row):
                if state[r] + 1 < col:
                    new_val = val - mat[r][state[r]] + mat[r][state[r] + 1]
                    state[r] += 1
                    if tuple(state) not in seen:
                        seen.add(tuple(state))
                        heapq.heappush(heap, [new_val, state[:]])
                    state[r] -= 1
        return val