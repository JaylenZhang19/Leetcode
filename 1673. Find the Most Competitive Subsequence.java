class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        Deque<Integer> deque = new ArrayDeque<>();
        int remain = nums.length;
        for(int i = 0; i < nums.length; i++){
            while (!deque.isEmpty() && deque.peekLast() > nums[i] && remain > (k - deque.size())) {
                deque.pollLast();
            }
            if(deque.size() < k){
                deque.addLast(nums[i]);
            }
            remain -= 1;
        }
        int[] result = new int[k];
        for(int i = 0; i < k; i++){
            result[i] = deque.pollFirst();
        }
        return result;
    }
}