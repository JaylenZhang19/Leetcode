class Solution {
    public int minSteps(String s, String t) {
        Map<Character, Integer> count1 = new HashMap<>();
        Map<Character, Integer> count2 = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            count1.put(s.charAt(i), count1.getOrDefault(s.charAt(i), 0) + 1);
            count2.put(t.charAt(i), count2.getOrDefault(t.charAt(i), 0) + 1);
        }
        int ans = 0;
        for(char key : count1.keySet()){
            ans += Math.max(0, count1.get(key) - count2.getOrDefault(key, 0));
        }
        return ans;
    }
}