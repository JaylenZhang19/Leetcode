class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Stack<Integer> stack = new Stack<Integer>();
        int l = nums.length;
        int r = 0;
        for(int i = 0; i < nums.length; i++){
            while(!stack.isEmpty() && nums[i] < nums[stack.peek()]){
                l = Math.min(l, stack.pop());
            }
            stack.push(i);
        }
        stack.clear();
        for(int i = nums.length-1; i >= 0; i--){
            while(!stack.isEmpty() && nums[i] > nums[stack.peek()]){
                r = Math.max(r, stack.pop());
            }
            stack.push(i);
        }
        return r - l > 0 ? r - l + 1 : 0;
    }
}