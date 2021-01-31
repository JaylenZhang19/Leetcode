class Solution {
    public boolean isNStraightHand(int[] hand, int W) {
        int n = hand.length;
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for(int val : hand){
            count.put(val, count.getOrDefault(val, 0) + 1);
        }
        while(!count.isEmpty()){
            int key = count.firstKey();
            int val = count.get(key);
            for(int i = 0; i < W; i++){
                if(count.getOrDefault(key + i, 0) - val >= 0 ){
                    count.put(key + i, count.get(key + i) - val);
                }
                else{
                    return false;
                }
                if(count.getOrDefault(key + i, 0) == 0) count.remove(key + i);
            }
        }
        return true;
    }
}