class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n = nums.length;
        if(n == 1){
            return nums[0];
        }
        if(nums[0] != nums[1]){
            return nums[0];
        }
        else if(nums[n-1] != nums[n-2]){
            return nums[n-1];
        }
        else{
            return helper(nums, 0, n-1);
        }
    }
    
    public int helper(int[] nums, int left, int right){
        if(left == right){
            return nums[left];
        }
        int mid = left + (right - left) / 2;
        if(nums[mid-1] != nums[mid] && nums[mid] != nums[mid+1]){
            return mid;
        }
        if(nums[mid] == nums[mid-1]){
            if((mid - left + 1) % 2 == 0){
                return helper(nums, mid+1, right);
            }
            else{
                return helper(nums, left, mid - 2);
            }
        }
        else{
            if((right - mid + 1) % 2 == 0){
                return helper(nums, left, mid-1);
            }
            else{
                return helper(nums, mid + 2, right);
            }
        }
    }
}