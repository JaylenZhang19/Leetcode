class Solution {
    public boolean splitArray(int[] nums) {
        
        
        int n = nums.length;
        if(n < 7){
            return false;
        }
        int[] sum = new int[n];
        sum[0] = nums[0];
        for(int i = 1; i < n; i++){
            sum[i] = nums[i] + sum[i-1];
        }
        
        for(int j = 3; j <= n-4; j++){
            HashSet<Integer> seen = new HashSet<>();
            for(int i = 1; i <= j-2; i++){
                if(sum[i-1] == sum[j-1] - sum[i]){
                    seen.add(sum[i-1]);
                }
            }
            for(int k = j+2; k <= n-2; k++){
                if(sum[n-1] - sum[k] == sum[k-1] - sum[j] && seen.contains(sum[k-1] - sum[j])){
                    return true;
                }
            }
        }
        return false;
    }
}