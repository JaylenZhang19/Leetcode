class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        int ret = 0;
        Arrays.sort(heaters);
        for(int h : houses){
            int left = 0, right = heaters.length-1;
            while(left < right){
                int mid = left + (right - left) / 2;
                if(heaters[mid] >= h){
                    right = mid;
                }
                else{
                    left = mid + 1;
                }
            }
            if(right > 0){
                int dist = Math.min(Math.abs(h - heaters[right]), Math.abs(h - heaters[right-1]));
                ret = Math.max(ret, dist);
            }
            else{
                ret = Math.max(ret, Math.abs(h - heaters[right]));
            }
        }
        return ret;
    }
}