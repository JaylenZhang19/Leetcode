class Solution {
    public int getFood(char[][] grid) {
        int row = grid.length;
        int column = grid[0].length;
        int x = -1, y = -1;
        for(int r = 0; r < row; r++){
            for(int c = 0; c < column; c++){
                if(grid[r][c] == '*'){
                    x = r;
                    y = c;
                    break;
                }
            }
        }

        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{x, y});
        boolean[][] seen = new boolean[row][column];
        for(boolean[] each_row : seen){
            Arrays.fill(each_row, false);
        }
        seen[x][y] = true;
        int step = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int[] cur = queue.poll();
                if(grid[cur[0]][cur[1]] == '#'){
                    return step;
                }
                for(int[] dir : new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}){
                    int newx = cur[0] + dir[0], newy = cur[1] + dir[1];
                    if(0 <= newx && newx < row && 0 <= newy && newy < column && grid[newx][newy] != 'X' && !seen[newx][newy]){
                        seen[newx][newy] = true;
                        queue.add(new int[]{newx, newy});
                    }
                }
            }
            step++;
        }
        return -1;
    }
}