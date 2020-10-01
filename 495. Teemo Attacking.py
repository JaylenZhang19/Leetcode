class Solution:
    def findPoisonedDuration(self, t: List[int], duration: int) -> int:
        return sum([min(duration, t[i + 1] - t[i]) for i in range(len(t) - 1)]) + duration if t else 0
                