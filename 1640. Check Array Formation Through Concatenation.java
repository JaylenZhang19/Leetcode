class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        Map<Integer, int[]> map = new HashMap<>();
        for(int[] p : pieces){
            map.put(p[0], p);
        }
        int index = 0;
        while(index < arr.length){
            if(!map.containsKey(arr[index])){
                return false;
            }
            for (int v : map.get(arr[index])){
                if(v != arr[index]){
                    return false;
                }
                index++;
            }
        }
        return true;
    }
}