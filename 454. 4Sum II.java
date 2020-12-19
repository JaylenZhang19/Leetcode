class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int a : A){
            for(int b : B){
                count.put(a+b, count.getOrDefault(a+b, 0)+1);
            }
        }
        int ret = 0;
        for(int c : C){
            for(int d : D){
                ret += count.getOrDefault(-(c+d), 0);
            }
        }
        return ret;
    }
}