class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int start = 0;
        int sum = 0;
        int ret = 0;
        Map<Integer, Integer> counter = new HashMap();
        for(int i = 0; i < nums.length; i++){
            int val = nums[i];
            sum += val;
            counter.put(val, counter.getOrDefault(val, 0) + 1);
            while(counter.get(val) > 1){
                sum -= nums[start];
                counter.put(nums[start], counter.get(nums[start]) - 1);
                start += 1;
            }
            ret = Math.max(ret, sum);
        }
        return ret;
    }
}