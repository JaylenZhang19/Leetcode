class Solution:
    def pathSum(self, nums: List[int]) -> int:
        levels = []
        for num in nums:
            l = num // 100
            if len(levels) < l:
                levels.append({})
            index, value = divmod(num % 100, 10)
            levels[l-1][index] = value

        ans = 0
        for i in range(len(levels) - 1):
            for index, value in levels[i].items():
                if index * 2 - 1 not in levels[i + 1] and index * 2 not in levels[i + 1]:
                    ans += value
                if index * 2 - 1 in levels[i + 1]:
                    levels[i + 1][index * 2 - 1] += value
                if index * 2 in levels[i + 1]:
                    levels[i + 1][index * 2] += value
        return sum([v for v in levels[-1].values()]) + ans