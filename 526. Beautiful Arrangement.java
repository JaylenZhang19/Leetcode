class Solution {
    int ret = 0;
    public int countArrangement(int n) {
        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);
        helper(visited, 0);
        return ret;
    }
    public void helper(boolean[] v, int index){
        if (index >= v.length-1){
            ret += 1;
            return;
        }
        for(int i = 1; i < v.length; i++){
            if(!v[i] && (i % (index + 1) == 0 || (index + 1) % i == 0)){
                v[i] = true;
                helper(v, index + 1);
                v[i] = false;
            }
        }
    }
}