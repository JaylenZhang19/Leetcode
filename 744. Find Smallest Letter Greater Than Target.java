class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        Arrays.sort(letters);
        for(char c : letters){
            if(target < c){
                return c;
            }
        }
        return letters[0];
    }
}