class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        int[] arr = new int[n*(n+1)/2];
        
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            arr[index++] = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                arr[index] = (arr[index-1] + nums[j]);
                index++;
            }
        }                  
        Arrays.sort(arr);
        
        int sum = 0;
        for (int i = left-1; i <= right-1; i++) {
            sum = (arr[i] + sum) % 1000000007;
        }
        
        return sum;
    
}
}