class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        product1 = collections.defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                product1[nums1[i] * nums1[j]] += 1
        product2 = collections.defaultdict(int)
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                product2[nums2[i] * nums2[j]] += 1
        count = 0
        for num in nums1:
            count += product2[num ** 2]
        for num in nums2:
            count += product1[num ** 2]
        return count