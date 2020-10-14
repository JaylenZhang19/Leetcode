class Solution {
public:
    map<int, int> memo{{1, 1}, {2, 2}};
    int climbStairs(int n) {
        if (memo.find(n) == memo.end()){
            int ans = climbStairs(n - 1) + climbStairs(n - 2);
            memo.insert({n, ans});
        }
        return memo.find(n)->second;
    }
};