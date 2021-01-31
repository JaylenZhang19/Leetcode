class Solution {
    public int[] threeEqualParts(int[] arr) {
        int[] wrong = new int[]{-1, -1};
        int n = arr.length;
        int s = 0;
        for(int val : arr) s += val;
        if(s == 0){
            return new int[]{0, n - 1};
        }
        if(s % 3 != 0) return wrong;
        int t = s / 3;
        int i1 = -1, j1 = -1, i2 = -1, j2 = -1, i3 = -1, j3 = -1;
        int su = 0;
        for(int i = 0; i < n; i++){
            if(arr[i] == 1){
                su += 1;
                if (su == 1) i1 = i;
                if(su == t) j1 = i;
                if(su == t + 1) i2 = i;
                if(su == 2 * t) j2 = i;
                if(su == 2 * t + 1) i3 = i;
                if(su == 3 * t) j3 = i;
            }
        }
        int[] part1 = Arrays.copyOfRange(arr, i1, j1 + 1);
        int[] part2 = Arrays.copyOfRange(arr, i2, j2 + 1);
        int[] part3 = Arrays.copyOfRange(arr, i3, j3 + 1);
        if(!Arrays.equals(part1, part2)) return wrong;
        if(!Arrays.equals(part1, part3)) return wrong;
        int x = i2 - j1 - 1;
        int y = i3 - j2 - 1;
        int z = n - j3 - 1;
        if(x < z || y < z) return wrong;
        return new int[]{j1 + z, j2 + z + 1};
    }
}