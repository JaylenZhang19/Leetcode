class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        Map<String, Integer> count = new HashMap();
        for(String word : A.split(" ")){
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        for(String word : B.split(" ")){
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        List<String> ret = new ArrayList();
        for(String word : count.keySet()){
            if(count.get(word) == 1){
                ret.add(word);
            }
        }
        return ret.toArray(new String[ret.size()]);
    }
}