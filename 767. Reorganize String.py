class Solution:
    def reorganizeString(self, S: str) -> str:
        count = collections.Counter(S)
        pq = [[-count[k], k] for k in count.keys()]
        heapq.heapify(pq)
        ret = ""
        while len(pq) > 1:
            num1, c1 = heapq.heappop(pq)
            num2, c2 = heapq.heappop(pq)
            ret = ret + c1 + c2
            num1 += 1
            num2 += 1
            if num1:
                heapq.heappush(pq, [num1, c1])
            if num2:
                heapq.heappush(pq, [num2, c2])
        if pq:
            if -pq[0][0] > 1:
                return ""
            else:
                return ret + pq[0][1]
        return ret