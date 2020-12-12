class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int index = n - 2;
        while(index >= 0 && nums[index] >= nums[index+1]){
            index--;
        }
        if(index >= 0){
            int j = n - 1;
            while(j >= 0 && nums[j] <= nums[index]){
                j--;
            }
            swap(nums, index, j);
        }
        int left = index + 1;
        int right = n - 1;
        while(left < right){
            swap(nums, left, right);
            left++;
            right--;
        }
        
    }
    
    private void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}