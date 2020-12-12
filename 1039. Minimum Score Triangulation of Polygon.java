class Solution {
    public int minScoreTriangulation(int[] A) {
        int n = A.length;
        int[][] dp = new int[n][n];
        return helper(dp, 0, n-1, A);
    }
    
    public int helper(int[][] dp, int start, int end, int[] A){
        if(dp[start][end] != 0){
            return dp[start][end];
        }
        if(end < start + 2){
            return 0;
        }
        int val = Integer.MAX_VALUE;
        for(int mid = start + 1; mid < end; mid++){
            int current_val = helper(dp, start, mid, A) + helper(dp, mid, end, A) + A[start] * A[mid] * A[end];
            val = Math.min(val, current_val);
        }
        dp[start][end] = val;
        return val;
    }
}