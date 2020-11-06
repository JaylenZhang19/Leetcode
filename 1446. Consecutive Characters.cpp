class Solution {
public:
    int maxPower(string s) {
        int n = s.size();
        vector<int> dp (n, 1);
        if(n == 1){
            return 1;
        }
        int maximum = 1;
        for(int i = 1; i < n; i++){
            if(s[i] == s[i-1]){
                dp[i] += dp[i-1];
                maximum = max(maximum, dp[i]);
            }
        }
        return maximum;
    }
};