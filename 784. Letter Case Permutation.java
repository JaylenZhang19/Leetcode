class Solution {
    List<String> ret = new ArrayList();
    public List<String> letterCasePermutation(String S) {
        helper(0, ret, S, new StringBuilder());
        return ret;
    }

    public void helper(int index, List<String> ret, String word, StringBuilder current){
        if(index == word.length()){
            ret.add(current.toString());
            return;
        }
        char c = word.charAt(index);
        if(Character.isDigit(c)){
            current.append(c);
            helper(index+1, ret, word, current);
            current.deleteCharAt(index);
        }else{
            current.append(c);
            helper(index+1, ret, word, current);
            current.deleteCharAt(index);
            if(Character.isLowerCase(c)){
                current.append(Character.toUpperCase(c));
            }
            else{
                current.append(Character.toLowerCase(c));
            }
            helper(index+1, ret, word, current);
            current.deleteCharAt(index);
        }
    }
}