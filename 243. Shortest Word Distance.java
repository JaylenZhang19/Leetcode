class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        ArrayList<ArrayList<Integer>> record = new ArrayList<ArrayList<Integer>>();
        int n = words.length;
        for(int i = 0; i < n; i++){
            if(words[i].equals(word1)){
                ArrayList<Integer> pair = new ArrayList<>();
                pair.add(i);
                pair.add(0);
                record.add(pair);
            }
            else if(words[i].equals(word2)){
                ArrayList<Integer> pair = new ArrayList<>();
                pair.add(i);
                pair.add(1);
                record.add(pair);
            }
        }
        
        int ret = Integer.MAX_VALUE;
        if(record.size() <= 1){
            return -1;
        }
        for(int i = 1; i < record.size(); i++){
            if((record.get(i).get(1) ^ record.get(i - 1).get(1)) == 1){
                ret = Math.min(ret, record.get(i).get(0) - record.get(i-1).get(0));
            }
        }
        return ret;
    }
}