class Solution {
    public String getSmallestString(int n, int k) {
        if(k < n || k > n * 26){
            return "";
        }
        StringBuilder sb = new StringBuilder();
        helper(n, k, sb);
        return sb.toString();
    }

    public void helper(int n, int k, StringBuilder sb){
        if(k == 0){
            return ;
        }
        int val = Math.max(1, k - 26 * (n - 1));
        sb.append((char)('a' + (val - 1)));
        n -= 1;
        k -= val;
        helper(n, k, sb);
    }
}