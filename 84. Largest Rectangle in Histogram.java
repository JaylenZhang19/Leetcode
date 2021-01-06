class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        int ret = 0;
        for(int i = 0; i < n; i++){
            while (!stack.isEmpty() && heights[i] <= heights[stack.peek()]){
                int index = stack.pop();
                int previous = stack.isEmpty()?-1:stack.peek();
                int h = heights[index];
                ret = Math.max(ret, h * (i - 1 - previous));
            }
            stack.add(i);
        }
        while(!stack.isEmpty()){
            int index = stack.pop();
            int previous = stack.isEmpty()?-1:stack.peek();
            int h = heights[index];
            ret = Math.max(ret, h * (n - 1 - previous));
        }
        return ret;
    }
}