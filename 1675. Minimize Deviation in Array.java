class Solution {
    public int minimumDeviation(int[] nums) {
        int ans = Integer.MAX_VALUE;
        int minimum = Integer.MAX_VALUE;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int num : nums){
            if(num % 2 == 0){
                minimum = Math.min(minimum, num);
                heap.add(-num);
            }else{
                minimum = Math.min(minimum, num * 2);
                heap.add(-num * 2);
            }

        }
        while(!heap.isEmpty()){
            int val = -heap.poll();
            ans = Math.min(ans, val - minimum);
            if(val % 2 == 1){
                break;
            }else{
                minimum = Math.min(minimum, val / 2);
                heap.add(-val / 2);
            }
        }
        return ans;
    }
}



class Solution {
    public int minimumDeviation(int[] nums) {
        int ans = Integer.MAX_VALUE;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                int temp = nums[i];
                heap.add(new int[] { temp, i });
                while (temp % 2 == 0) {
                    temp /= 2;
                    heap.add(new int[] { temp, i });
                }
            } else {
                heap.add(new int[] { nums[i], i });
                heap.add(new int[] { nums[i] * 2, i });
            }
        }
        List<int[]> seen = new ArrayList<>();
        int start = 0;
        int include = nums.length;
        int[] need_include = new int[nums.length];
        Arrays.fill(need_include, 1);

        while(!heap.isEmpty()){
            int[] cur = heap.poll();
            int val = cur[0], index = cur[1];
            seen.add(cur);
            need_include[index] -= 1;
            if(need_include[index] == 0){
                include -= 1;
            }
            if(include == 0){
                while(need_include[seen.get(start)[1]] < 0){
                    need_include[seen.get(start)[1]] += 1;
                    start += 1;
                }
                ans = Math.min(ans, val - seen.get(start)[0]);
            }
        }
        return ans;
    }
}






