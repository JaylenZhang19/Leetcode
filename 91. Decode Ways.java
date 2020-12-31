class Solution {
    int ret = 0;
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n];
        for(int index = n - 1; index >= 0; index--){
            if (s.charAt(index) == '0'){
                continue;
            }
            if(s.charAt(index) != '0'){
                dp[index] += index + 1 < s.length()? dp[index+1] : 1;
            }
            if(index + 1 < s.length()){
                int val = Integer.parseInt(s.substring(index, index+2));
                if(val <= 26 && val > 0){
                    dp[index] += index + 2 < s.length()? dp[index+2] : 1;
                }
            }
        }
        return dp[0];
        
    }
}