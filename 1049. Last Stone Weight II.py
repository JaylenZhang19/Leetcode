class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summation = sum(stones)
        print(summation)
        previous = set()
        previous.add(0)
        for stone in stones:
            position = list(previous)
            for p in position:
                if p + stone <= (summation // 2):
                    previous.add(p + stone)
        print(previous)

        return summation - max(previous) * 2

