class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        Map<Integer, Integer> seen = new HashMap<>();
        
        int res = 0;
        for(int val : time){
            val = val % 60;
            res += seen.getOrDefault((60 - val) % 60, 0);
            seen.put(val, seen.getOrDefault(val, 0) + 1);
        }
        return res;
    }
}