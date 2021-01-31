class Solution {
    public int validSubarrays(int[] nums) {
        int ret = 0;
        Stack<Integer> stack = new Stack<>();
        for(int val : nums){
            while(!stack.isEmpty() && val < stack.peek()){
                stack.pop();
            }
            stack.add(val);
            ret += stack.size();
        }
        return ret;
    }
}