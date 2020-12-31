class Solution {
    public String maximumBinaryString(String binary) {
        int n = binary.length();
        int zeros = 0;
        int leading_ones = 0;
        for(int i = 0; i < n; i++){
            if(binary.charAt(i) == '0'){
                zeros++;
            }
            if(zeros == 0){
                leading_ones++;
            }
        }
        StringBuilder sb = new StringBuilder("1".repeat(n));
        if(leading_ones == n){
            return sb.toString();
        }
        sb.setCharAt(leading_ones + zeros - 1, '0');
        return sb.toString();
    }
}