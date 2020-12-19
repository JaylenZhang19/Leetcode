class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int row = matrix.length;
        if(row == 0){
            return matrix;
        }
        int column = matrix[0].length;
        int[][] ret = new int[row][column];
        for(int[] each_row : ret){
            Arrays.fill(each_row, Integer.MAX_VALUE);
        }
        Queue<int[]> queue = new LinkedList<>();
        for(int r = 0; r < row; r++){
            for(int c = 0; c < column; c++){
                if (matrix[r][c] == 0){
                    queue.add(new int[]{r, c});
                    ret[r][c] = 0;
                }
            }
        }
        while(!queue.isEmpty()){
            int[] coordinate = queue.poll();
            int x = coordinate[0];
            int y = coordinate[1];
            int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for(int i = 0; i < 4; i++){
                int x_ = dir[i][0];
                int y_ = dir[i][1];
                int newx = x_ + x;
                int newy = y_ + y;
                if(0 <= newx && newx < row && 0 <= newy && newy < column && matrix[newx][newy] == 1){
                    if(ret[newx][newy] > ret[x][y] + 1){
                        ret[newx][newy] = ret[x][y] + 1;
                        queue.add(new int[]{newx, newy});
                    }
                }
            }
        }
        return ret;
    }
}