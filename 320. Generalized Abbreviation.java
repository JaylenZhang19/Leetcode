class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> ans = new ArrayList<>();
        helper(0, 0, ans, word, new StringBuffer());
        return ans;
    }

    public void helper(int cur_index, int repeat, List<String> ans, String word, StringBuffer sb){
        int n = sb.length();
        if(cur_index == word.length()){
            if(repeat != 0){
                sb.append(repeat);
            }
            ans.add(sb.toString());
        }
        else{
            // as number
            helper(cur_index + 1, repeat + 1, ans, word, sb);
            // as digit
            if(repeat != 0){
                sb.append(repeat);
            }
            sb.append(word.charAt(cur_index));
            helper(cur_index + 1, 0, ans, word, sb);
        }
        sb.setLength(n);

    }
}