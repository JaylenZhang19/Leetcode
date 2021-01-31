class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> nums.get(a[0]).get(a[1])));
        int maximum = Integer.MIN_VALUE;
        int ret_min = -((int)Math.pow(10, 5) + 1), ret_max = (int)Math.pow(10, 5) + 1;
        for(int i = 0; i < nums.size(); i++){
            heap.add(new int[]{i, 0});
            maximum = Math.max(maximum, nums.get(i).get(0));
        }
        int dif = ret_max - ret_min;

        while(!heap.isEmpty()){
            int[] coordinate = heap.poll();
            int row = coordinate[0], col = coordinate[1];
            int val = nums.get(row).get(col);
            if(maximum - val < dif){
                dif = maximum - val;
                ret_min = val;
                ret_max = maximum;
            }
            if(col + 1 == nums.get(row).size()){
                break;
            }else{
                maximum = Math.max(maximum, nums.get(row).get(col + 1));
                heap.add(new int[]{row, col + 1});
            }
        }
        return new int[]{ret_min, ret_max};
    }
}