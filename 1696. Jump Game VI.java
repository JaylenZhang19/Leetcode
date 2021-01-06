class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b)->a[0] - b[0]);
        for(int i = 0; i < n; i++){
            if(!heap.isEmpty()){
                int[] largest = heap.poll();
                while(largest[1] < i - k){
                    largest = heap.poll();
                }
                dp[i] = nums[i] + dp[largest[1]];
                if(largest[1] > i - k){
                    heap.add(largest);
                }
            }
            heap.add(new int[]{-dp[i], i});
        }
        return dp[n-1];
    }
}