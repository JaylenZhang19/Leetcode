class Solution {
    public int minimumEffortPath(int[][] heights) {
        int row = heights.length;
        int column = heights[0].length;
        int[][] record = new int[row][column];
        for(int[] each_row : record){
            Arrays.fill(each_row, Integer.MAX_VALUE);
        }
        record[row-1][column-1] = 0;
        Queue<int[]> queue = new LinkedList();
        queue.add(new int[]{row-1, column-1});
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for(int i = 0; i < 4; i++){
                int newx = dirs[i][0] + x;
                int newy = dirs[i][1] + y;
                if(newx >= 0 && newx < row & newy >= 0 && newy < column){
                    if(Math.max(Math.abs(heights[newx][newy] - heights[x][y]), record[x][y]) < record[newx][newy]) {
                        record[newx][newy] = Math.max(Math.abs(heights[newx][newy] - heights[x][y]), record[x][y]);
                        queue.add(new int[]{newx, newy});
                    }
                }
            }
        }
        return record[0][0];
    }
}