class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> ans = new ArrayList<>();
        for(String word : queries){
            int i = 0, j = 0;
            boolean flag = true;
            while(i < word.length() && j < pattern.length()){
                char c1 = word.charAt(i);
                char c2 = pattern.charAt(j);
                if(c1 == c2){
                    i += 1;
                    j += 1;
                }else if(!Character.isLowerCase(c1)){
                    flag = false;
                    break;
                }else{
                    i += 1;
                }
            }
            while(i < word.length()){
                char c1 = word.charAt(i);
                if(!Character.isLowerCase(c1)){
                    flag = false;
                    break;
                }
                i += 1;
            }
            if(j < pattern.length()){
                flag = false;
            }
            ans.add(flag);
        }
        return ans;
    }
}