class Solution {
    public String multiply(String num1, String num2) {
        int[] r = new int[num1.length() + num2.length()];
        for (int i = num1.length() - 1; i >= 0; i--) {
            for (int j = num2.length() - 1; j >= 0; j--) {
                int k = num1.length() - 1 - i + num2.length() - 1 - j;
                int t = Character.digit(num1.charAt(i), 10) * Character.digit(num2.charAt(j), 10) + r[k];
                r[k] = t % 10;
                r[k + 1] += t / 10;
            }
        }
        int i = r.length - 1;
        while (i >= 0 && r[i] == 0) {
            i--;
        }
        if (i == -1) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (; i >= 0; i--) {
            sb.append(r[i]);
        }
        return sb.toString();
    }
}