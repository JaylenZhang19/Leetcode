class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        vector<int> count;
        count.assign(K, 0);
        count[0] = 1;
        
        int previous = 0;
        int ans = 0;
        for(auto num: A){
            int current = ((previous + num) % K + K) % K;
            ans += count[current];
            count[current] += 1;
            previous = current;
        }
        return ans;
    }
};