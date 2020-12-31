class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        int row = matrix.length;
        if (row == 0){
            return new int[]{};
        }
        int column = matrix[0].length;
        int[] ret = new int[row * column];
        Deque<int[]> current = new ArrayDeque<>();
        current.add(new int[]{0, 0});
        int bottom_up = 1;
        int index = 0;
        while(!current.isEmpty()){
            int size = current.size();
            Deque<int[]> next = new ArrayDeque<>();
            for(int i = 0; i < size; i++){
                int[] coordinate = current.poll();
                ret[index] = matrix[coordinate[0]][coordinate[1]];
                index ++;
                if(bottom_up == 1){
                    if(i == 0){
                        if(coordinate[0] + 1 < row){
                            next.add(new int[]{coordinate[0] + 1, coordinate[1]});
                        }
                    }
                    if(coordinate[1] + 1 < column){
                        next.add(new int[]{coordinate[0], coordinate[1] + 1});
                    }
                }
                else{
                    if(i == 0){
                        if(coordinate[1] + 1 < column){
                            next.add(new int[]{coordinate[0], coordinate[1] + 1});
                        }
                    }
                    if(coordinate[0] + 1 < row){
                        next.add(new int[]{coordinate[0] + 1, coordinate[1]});
                    }
                }
                
            }
            bottom_up ^= 1;
                while(!next.isEmpty()){
                    current.add(next.pollLast());
                }
        }
        return ret;
    }
}