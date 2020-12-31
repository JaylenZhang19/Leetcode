class Solution {
    public int[] processQueries(int[] queries, int m) {
        int n = queries.length;
        int[] ret = new int[n];
        int index = 0;
        Deque<Integer> deque1 = new ArrayDeque<>();
        for(int i = 1; i <= m; i++){
            deque1.add(i);
        }
        for(int i = 0; i < n; i++){
            Deque<Integer> deque2 = new ArrayDeque<>();
            int target = queries[i];
            int current_index = 0;
            while(!deque1.isEmpty()){
                int val = deque1.pollFirst();
                if(val == target){
                    ret[index] = current_index;
                    index++;
                    deque2.addFirst(val);
                }else{
                    deque2.addLast(val);
                }
                current_index++;
            }
            deque1 = deque2;
        }
        return ret;
        
    }
}


