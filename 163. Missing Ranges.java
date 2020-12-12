class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        int n = nums.length;
        List<String> ret = new ArrayList();
        if(n == 0){
            ret.add(helper(lower, upper));
            return ret;
        }
        
        if(nums[0] > lower){
            ret.add(helper(lower, nums[0] - 1));
        }
        for(int i = 1; i < n; i++){
            if(nums[i] - nums[i-1] > 1){
                ret.add(helper(nums[i-1] + 1, nums[i] - 1));
            }
        }
        if(nums[n-1] < upper){
            ret.add(helper(nums[n-1] + 1, upper));
        }
        return ret;
    }
    
    private String helper(int left, int right){
        if(left == right){
            return String.valueOf(left);
        }else{
            return left + "->" + right;
        }
    }
}