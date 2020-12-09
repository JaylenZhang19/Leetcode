class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int ret = 0;
        for(int index = 0; index < points.length; index++){
            Map<Integer, Integer> seen = new HashMap<>();
            
            for(int j = 0; j < points.length; j++){
                if(j == index){
                    continue;
                }
                int x = points[index][0] - points[j][0];
                int y = points[index][1] - points[j][1];
                int distance = x * x + y * y;
                seen.put(distance, seen.getOrDefault(distance, 0) + 1);
            }
            for(int key : seen.keySet()){
                int val = seen.get(key);
                ret += val * (val - 1);
            }
        }
        return ret;
    }
}