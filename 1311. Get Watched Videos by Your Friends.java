class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        int[] levels = new int[friends.length];
        Arrays.fill(levels, -1);
        levels[id] = 0;
        Map<String, Integer> count = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(id);
        int current_level = 0;
        while (!queue.isEmpty()){
            current_level++;
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int person = queue.poll();
                for(int f : friends[person]){
                    if(levels[f] == -1){
                        levels[f] = current_level;
                        queue.add(f);
                        if(current_level == level){
                            for(String movie : watchedVideos.get(f)){
                                count.put(movie, count.getOrDefault(movie, 0) + 1);
                            }
                        }
                    }
                }
            }
        }
        List<String>  ret = new ArrayList<>();
        for(String m : count.keySet()){
            ret.add(m);
        }
        Collections.sort(ret);
        Collections.sort(ret, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return count.get(o1).compareTo(count.get(o2));
            }
        });
        return ret;
    }
}