class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        // find the depth
        int depth = find_depth(nestedList);
        return helper(nestedList, depth);
    }
    
    public int find_depth(List<NestedInteger> nlist){
        int current_depth = 1;
        for(NestedInteger item : nlist){
            if(!item.isInteger()){
                current_depth = Math.max(find_depth(item.getList()) + 1, current_depth);
            }
        }
        return current_depth;
    }
    
    public int helper(List<NestedInteger> nlist, int d){
        int ret = 0;
        for(NestedInteger item : nlist){
            if(item.isInteger()){
                ret += d * item.getInteger();
            }
            else{
                ret += helper(item.getList(), d - 1);
            }
        }
        return ret;
    }
    
}