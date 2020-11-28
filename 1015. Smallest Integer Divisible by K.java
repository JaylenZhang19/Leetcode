class Solution {
    public int smallestRepunitDivByK(int K) {
        int remainder = 0;
        for(int length = 1; length <= K + 1; length++){
            remainder = (remainder * 10 + 1) % K;
            if(remainder == 0){
                return length;
            }
        }
        return -1;
    }
}