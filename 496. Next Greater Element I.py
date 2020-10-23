class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pair = {}
        for num in nums2:
            pair[num] = -1
        stack = []
        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    pair[stack[-1]] = num
                    stack.pop()
                stack.append(num)
        return [pair[num] for num in nums1]
        