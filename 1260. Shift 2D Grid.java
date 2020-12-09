class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int row = grid.length;
        int column = grid[0].length;
        List<List<Integer>> ret = new ArrayList<>();
        for(int r = 0; r < row; r++){
            List<Integer> new_row = new ArrayList<>();
            for(int c = 0; c < column; c++){
                new_row.add(0);
            }
            ret.add(new_row);
        }
        k = k % (row * column);
        for(int r = 0; r < row; r++){
            for(int c = 0; c < column; c++){
                int new_col = (c + k) % column;
                int step = (c + k) / column;
                int new_row = (r + step) % row;
                ret.get(new_row).set(new_col, grid[r][c]);
            }
        }
        return ret;
    }
}