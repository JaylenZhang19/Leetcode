class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for(int num : nums){
            if(num > second){
                return true;
            }
            else if(num < first){
                second = first;
                first = num;
            }
            else if(num < second){
                second = num;
            }
        }
        return false;
    }
}