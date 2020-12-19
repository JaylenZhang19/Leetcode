class Solution {
    public int maxDepth(String s) {
        int n = s.length();
        int ret = 0;
        Stack<Integer> stack = new Stack();
        for(int i = 0; i < n; i++){
            if(s.charAt(i) == '('){
                stack.push(i);
                ret = Math.max(ret, stack.size());
            }
            else if(s.charAt(i) == ')'){
                stack.pop();
            }
            
        }
        return ret;
    }
}