class Solution {
    public boolean judgeCircle(String moves) {
        Map<Character, Integer> counter = new HashMap<>();
        for(int i = 0; i < moves.length(); i++){
            counter.put(moves.charAt(i), counter.getOrDefault(moves.charAt(i), 0) + 1);
        }
        if(counter.getOrDefault('U', 0).equals(counter.getOrDefault('D', 0)) && counter.getOrDefault('L', 0).equals(counter.getOrDefault('R', 0))){
            return true;
        }
        return false;
    }
}