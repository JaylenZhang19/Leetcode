class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int ret = 0;
        Map<Character, Integer> count = new HashMap<>();
        int repeat = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            count.put(c, count.getOrDefault(c, 0) + 1);
            if(count.get(c) > 1){
                repeat += 1;
            }
            while(repeat > 0){
                char start_c = s.charAt(start);
                start++;
                count.put(start_c, count.get(start_c) - 1);
                if(count.get(start_c) > 0){
                    repeat -= 1;
                }
            }
            ret = Math.max(ret, i - start + 1);
        }
        return ret;
        
    }
}