class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        int n = aliceValues.length;
        int[][] s = new int[n][2];
        for(int i = 0; i < n; i++){
            s[i][0] = aliceValues[i] + bobValues[i];
            s[i][1] = i;
        }
        Arrays.sort(s, (a, b) -> Integer.compare(b[0], a[0]));
        int a = 0;
        int b = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                a += aliceValues[s[i][1]];
            } else {
                b += bobValues[s[i][1]];
            }
        }
        return a == b ? 0 : a > b ? 1 : -1;
    }
}