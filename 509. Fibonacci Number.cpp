class Solution {
public:
    map<int, int> memo = {{0, 0}, {1, 1} };

    int fib(int N){
        if(N == 0) {
            return 0;
        }
        if (N == 1){
            return 1;
        }
        int ans = fib(N - 1) + fib(N - 2);
        if (memo.find(N) == memo.end()){
            memo.insert(pair<int, int>(N, ans));
        }
        return memo.find(N)->second;
    }
};