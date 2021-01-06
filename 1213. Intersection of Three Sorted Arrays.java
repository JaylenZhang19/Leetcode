class Solution {
    public List<Integer> arraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        List<Integer> ret = new ArrayList();
        Set<Integer> seen1 = new HashSet();
        Set<Integer> seen2 = new HashSet();
        for(int val : arr1){
            seen1.add(val);
        }
        for(int val : arr2){
            seen2.add(val);
        }
        for(int val : arr3){
            if(seen1.contains(val) && seen2.contains(val)){
                ret.add(val);
            }
        }
        return ret;
    }
}