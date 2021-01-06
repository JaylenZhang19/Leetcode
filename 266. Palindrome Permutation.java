class Solution {
    public boolean canPermutePalindrome(String s) {
        Map<Character, Integer> counter = new HashMap();
        int odd = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            counter.put(c, counter.getOrDefault(c, 0) + 1);
            if(counter.get(c) % 2 == 0){
                odd -= 1;
            }
            else{
                odd += 1;
            }
        }
        return odd <= 1?true:false;
    }
}