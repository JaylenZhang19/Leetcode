class Solution {
    public int maxSum(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        long val1 = 0, val2 = 0;
        int mod = (int)Math.pow(10, 9) + 7;
        while(i < nums1.length && j < nums2.length){
            if(nums1[i] == nums2[j]){
                val1 += nums1[i];
                val2 += nums2[j];
                i += 1;
                j += 1;
                long val = Math.max(val1, val2);
                val1 = val;
                val2 = val;
            }else if(nums1[i] < nums2[j]){
                val1 += nums1[i];
                i += 1;
            }else{
                val2 += nums2[j];
                j += 1;
            }
        }
        while(i < nums1.length){
            val1 += nums1[i];
            i += 1;
        }
        while(j < nums2.length){
            val2 += nums2[j];
            j += 1;
        }
        int ret = Math.max(val1, val2) % 1000000007;
        return ret;
    }
}