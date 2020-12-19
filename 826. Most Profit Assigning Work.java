class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int n = difficulty.length;
        int[][] job = new int[n][2];
        for(int i = 0; i < n; i++){
            job[i][0] = difficulty[i];
            job[i][1] = profit[i];
        }
        Arrays.sort(job, (a, b) -> a[0] - b[0]);
        Arrays.sort(worker);
        int ret = 0;
        for(int w : worker){
            int index = 0;
            int best = 0;
            while (index < n && w >= job[index][0]){
                best = Math.max(best, job[index][1]);
                index++;
            }
            ret += best;
        }
        return ret;
    }
}