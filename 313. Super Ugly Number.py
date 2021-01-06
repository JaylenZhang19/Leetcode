class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = set()
        val = 1
        for _ in range(n):
            val = heapq.heappop(heap)
            for p in primes:
                new_val = p * val
                if new_val not in seen:
                    seen.add(new_val)
                    heapq.heappush(heap, new_val)
        return val
        