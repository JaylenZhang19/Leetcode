class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return 
        val = nums2.pop(0)
        index = 0
        while index < m:
            if nums1[index] >= val:
                break
            index += 1
        for i in range(len(nums1) - 2, index - 1, -1):
            nums1[i + 1] = nums1[i]
        nums1[index] = val
        self.merge(nums1, m + 1, nums2, n - 1)
        