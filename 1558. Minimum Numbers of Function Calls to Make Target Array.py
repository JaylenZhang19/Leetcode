class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        s = sum(nums)
        while s > 0:
            for i in range(n):
                if nums[i] == 0:
                    continue
                elif nums[i] == 1:
                    nums[i] -= 1
                    s -= 1
                    ret += 1
                elif nums[i] % 2 == 1:
                    dif = nums[i] - ((nums[i]-1)//2)
                    s -= dif
                    nums[i] = (nums[i]-1)//2
                    ret += 1
                else:
                    nums[i] = nums[i] // 2
                    s -= nums[i]
            ret += 1
            
        
        return ret - 1 if ret != 0 else 0
            