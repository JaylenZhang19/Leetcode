class Solution {
    public int minJumps(int[] arr) {
        int n = arr.length;
        Map<Integer, LinkedList<Integer>> graph = new HashMap<>();
        for(int i = 0; i < n; i++){
            if(graph.containsKey(arr[i])){
                graph.get(arr[i]).add(i);
            }else{
                LinkedList<Integer> list = new LinkedList<>();
                list.add(i);
                graph.put(arr[i], list);
            }
        }
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(0);
        int step = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int current = queue.poll();
                if(current == n - 1){
                    return step;
                }
                for(int nei : graph.get(arr[current])){
                    if(!visited.contains(nei)){
                        queue.add(nei);
                        visited.add(nei);
                    }
                }
                graph.get(arr[current]).clear();
                if(current + 1 < n && !visited.contains(current + 1)){
                    queue.add(current + 1);
                    visited.add(current + 1);
                }
                if(current - 1 >= 0 && !visited.contains(current - 1)){
                    queue.add(current - 1);
                    visited.add(current - 1);
                }
            }
            step++;
        }
        return -1;
    }
}