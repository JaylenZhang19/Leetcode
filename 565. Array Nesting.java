class Solution {
    public int arrayNesting(int[] nums) {
        int ret = 0;
        for(int i = 0; i < nums.length; i++){
            int count = 0;
            int current_index = i;
            while(nums[current_index] != -1){
                count++;
                int next_index = nums[current_index];
                nums[current_index] = -1;
                current_index = next_index;
            }
            ret = Math.max(count, ret);
        }
        return ret;
    }
}