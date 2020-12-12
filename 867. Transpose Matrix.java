class Solution {
    public int[][] transpose(int[][] A) {
        int row = A.length;
        int column = A[0].length;
        int[][] ret = new int[column][row];
        for(int r = 0; r < row; r++){
            for(int c = 0; c < column; c++){
                ret[c][r] = A[r][c];
            }
        }
        return ret;
    }
}