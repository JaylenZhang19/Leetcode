class Solution {
    public int maxBoxesInWarehouse(int[] boxes, int[] warehouse) {
        Stack<Integer> stack = new Stack();
        int threshold = Integer.MAX_VALUE;
        for(int i = 0; i < warehouse.length; i++){
            threshold = Math.min(threshold, warehouse[i]);
            stack.add(threshold);
        }
        int ans = 0;
        Arrays.sort(boxes);
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