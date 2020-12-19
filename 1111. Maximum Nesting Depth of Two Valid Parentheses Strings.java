class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int n = seq.length();
        int[] ret = new int[n];
        Stack<Integer> stack = new Stack();
        for(int i = 0; i < n; i++){
            if(seq.charAt(i) == '('){
                stack.push(i);
            }else{
                int val = (stack.size() + 1) % 2;
                ret[stack.pop()] = val;
                ret[i] = val;
            }
        }
        return ret;
    }
}