class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        if(nums.size() == 1){
            return nums[0];
        }
        return max(helper(nums, 0, nums.size() - 1), helper(nums, 1, nums.size()));
    }
    
    int helper(vector<int>& nums, int start, int end){
        int pre_take = 0, pre_notake = 0;
        for(int i = start; i < end; i++){
            int current_take = pre_notake + nums[i];
            int current_notake = max(pre_take, pre_notake);
            pre_take = current_take;
            pre_notake = current_notake;
        }
        return max(pre_take, pre_notake);
    }
    
   
};