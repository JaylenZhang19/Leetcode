class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        ret[0] = nums[0];
        for(int i = 1; i < n; i++){
            ret[i] = ret[i-1] * nums[i];
        }
        int r = 1;
        for(int i = n-1; i >= 0; i--){
            ret[i] = (i-1 >= 0) ? (r * ret[i-1]) : r;
            r *= nums[i];
        }
        return ret;
    }
}