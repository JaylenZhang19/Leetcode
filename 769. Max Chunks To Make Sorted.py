class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        longest = arr[0]
        count = 0
        index = 0
        find_start = False
        while index < n:
            if arr[index] == start:
                find_start = True
            longest = max(longest, arr[index])
            if longest == index and find_start:
                count += 1
                find_start = False
                start = index + 1
            index += 1
        return count