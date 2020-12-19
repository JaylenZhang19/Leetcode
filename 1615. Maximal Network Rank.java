class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for(int i = 0; i < roads.length; i++){
            int city1 = roads[i][0];
            int city2 = roads[i][1];
            if(graph.containsKey(city1)){
                graph.get(city1).add(city2);
            }else{
                Set<Integer> seen = new HashSet<>();
                seen.add(city2);
                graph.put(city1, seen);
            }
            if(graph.containsKey(city2)){
                graph.get(city2).add(city1);
            }else{
                Set<Integer> seen = new HashSet<>();
                seen.add(city1);
                graph.put(city2, seen);
            }
        }
        int ret = 0;
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                int val = 0;
                if(graph.containsKey(i)){
                    val += graph.get(i).size();
                }
                if(graph.containsKey(j)){
                    val += graph.get(j).size();
                    if(graph.get(j).contains(i)){
                        val -= 1;
                    }
                }
                ret = Math.max(ret, val);
            }
        }
        return ret;
    }
}