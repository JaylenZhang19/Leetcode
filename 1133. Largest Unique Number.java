class Solution {
    public int largestUniqueNumber(int[] A) {
        Arrays.sort(A);
        int ret = Integer.MAX_VALUE;
        int count = 0;
        for(int start = A.length-1; start >= 0; start--){
            if(A[start] != ret){
                if(count == 1){
                    return ret;
                }else{
                    count = 1;
                    ret = A[start];
                }
            }else{
                count++;
            }
        }
        if(count == 1){
            return ret;
        }else{
            return -1;
        }
    }
}