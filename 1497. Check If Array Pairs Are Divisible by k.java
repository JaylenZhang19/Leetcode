class Solution {
    public boolean canArrange(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int current_pairs = 0;
        for(int val : arr){
            int remain = val % k;
            if (remain < 0){
                remain += k;
            }
            int count = map.getOrDefault(k - remain, 0);
            if ( count > 0){
                map.put(k - remain, --count);
                current_pairs++;
            }else{
                int key_count = map.getOrDefault(remain, 0);
                map.put(remain, key_count + 1);
            }
        }
        if(map.getOrDefault(0, 0) / 2 + current_pairs == arr.length / 2){
            return true;
        }else{
            return false;
        }
        
    }
}