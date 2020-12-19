class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        Queue<Integer> heap = new PriorityQueue<>((a, b) -> a - b);
        for(int i = 0; i < heights.length-1; i++){
            int diff = heights[i+1] - heights[i];
            if(diff <= 0){
                continue;
            }
            heap.add(diff);
            if(heap.size() > ladders){
                bricks -= heap.remove();
            }
            if(bricks < 0){
                return i;
            }
        }
        return heights.length - 1;
    }
}