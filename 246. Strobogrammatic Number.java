class Solution {
    public boolean isStrobogrammatic(String num) {
        int left = 0, right = num.length() - 1;
        if(left == right){
            if(num.equals("1") || num.equals("8") || num.equals("0")) return true;
            return false;
        }

        while (left < right){
            if((num.charAt(left) == '6' && num.charAt(right) == '9') || (num.charAt(left) == '9' && num.charAt(right) == '6') || (num.charAt(left) == '8' && num.charAt(right) == '8') || (num.charAt(left) == '1' && num.charAt(right) == '1') || (num.charAt(left) == '0' && num.charAt(right) == '0')){
                left += 1;
                right -= 1;
            }
            else{
                return false;
            }

        }
        if(left == right){
            if(num.charAt(left) == '1' || num.charAt(left) == '8' || num.charAt(left) == '0'){
                return true;
            }
            return false;
        }
        return true;
    }
}