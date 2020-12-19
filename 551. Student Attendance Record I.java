class Solution {
    public boolean checkRecord(String s) {
        int count = 0;
        boolean find = false;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'A'){
                count++;
            }
            if(i >= 2 && s.charAt(i-2) == s.charAt(i-1) && s.charAt(i-1) == s.charAt(i) && s.charAt(i) == 'L'){
                find = true;
            }
        }
        if(count > 1 || find){
            return false;
        }
        return true;
    }
}