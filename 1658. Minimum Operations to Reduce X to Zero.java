class Solution {
    public int minOperations(int[] nums, int x) {
        int sum = 0;
        for(int num : nums){
            sum += num;
        }
        int target = sum - x;
        int start = 0;
        int current_sum = 0;
        int ret = -1;
        for(int i = 0; i < nums.length; i++){
            current_sum += nums[i];
            while(start < nums.length && current_sum > target ){
                current_sum -= nums[start];
                start++;
            }
            if(current_sum == target){
                ret = Math.max(ret, i - start + 1);
            }
        }
        return (ret == -1)?-1:nums.length - ret;
    }
}