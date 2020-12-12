class Solution {
    public int removeDuplicates(int[] nums) {
        boolean have_two = false;
        int p1 = 0;
        int p2 = p1 + 1;
        while(p2 < nums.length){
            if(nums[p1] == nums[p2] && !have_two){
                p1++;
                nums[p1] = nums[p2];
                have_two = true;
            }
            else if(nums[p1] != nums[p2]){
                have_two = false;
                p1++;
                nums[p1] = nums[p2];
            }
            p2++;
        }
        return p1 + 1;
    }
}