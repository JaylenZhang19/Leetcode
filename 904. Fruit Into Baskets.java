class Solution {
    public int totalFruit(int[] tree) {
        int n = tree.length;
        Map<Integer, Integer> count = new HashMap();
        int start = 0;
        int end = 0;
        int ret = 0;
        while(end < n){
            count.put(tree[end], count.getOrDefault(tree[end], 0) + 1);
            while(count.size() > 2){
                count.put(tree[start], count.get(tree[start]) - 1);
                if(count.get(tree[start]) == 0){
                    count.remove(tree[start]);
                }
                start++;
            }
            end++;
            ret = Math.max(ret, end - start);
        }
        return ret;
    }
}