class Solution {
    public int maxBoxesInWarehouse(int[] boxes, int[] warehouse) {
        Stack<Integer> stack = new Stack<>();
        int left = 0, right = warehouse.length - 1;
        int left_min = Integer.MAX_VALUE, right_min = Integer.MAX_VALUE;
        while(left <= right){
            left_min = Math.min(left_min, warehouse[left]);
            right_min = Math.min(right_min, warehouse[right]);
            if(left_min >= right_min){
                stack.add(left_min);
                left += 1;
            }else{
                stack.add(right_min);
                right -= 1;
            }
        }
        Arrays.sort(boxes);
        int ans = 0;
        for(int i = 0; i < boxes.length; i++){
            while(!stack.isEmpty() && stack.peek() < boxes[i]){
                stack.pop();
            }
            if(!stack.isEmpty()){
                ans += 1;
                stack.pop();
            }
        }
        return ans;
    }
}