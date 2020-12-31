class Solution {
    public double averageWaitingTime(int[][] customers) {
        double s = 0;
        int n = customers.length;
        int end_time = 0;
        for(int i = 0; i < n; i++){
            int start_time = Math.max(end_time, customers[i][0]);
            int finish_time = start_time + customers[i][1];
            s += finish_time - customers[i][0];
            end_time = finish_time;
        }
        return s / n;
    }
}