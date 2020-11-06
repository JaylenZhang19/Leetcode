class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        pq = []
        for key, val in count.items():
            pq.append([-val, key])
        heapq.heapify(pq)
        ans = []
        while len(pq) >= 2:
            number1, k1 = heapq.heappop(pq)
            number2, k2 = heapq.heappop(pq)
            ans.append(k1)
            ans.append(k2)
            number1 += 1
            number2 += 1
            if number1:
                heapq.heappush(pq, [number1, k1])
            if number2:
                heapq.heappush(pq, [number2, k2])
        if pq:
            ans.append(pq[0][1])
        return ans