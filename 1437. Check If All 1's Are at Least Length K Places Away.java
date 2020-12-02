class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        if(k == 0){
            return true;
        }
        int previous_index = -1;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                if(previous_index != -1 && i - previous_index <= k){
                    return false;
                }
                previous_index = i;
            }
        }
        return true;
    }
}