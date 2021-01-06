class Solution {
    public boolean canWin(String s) {
        char[] list = s.toCharArray();
        return helper(list);
    }
    public boolean helper(char[] list){
        int n = list.length;
            for(int i = 0; i < n-1; i++){
                if(list[i] == '+' && list[i+1] == '+'){
                    list[i] = '-';
                    list[i+1] = '-';
                    if(!helper(list)){
                        list[i] = '+';
                        list[i+1] = '+';
                        return true;
                    }
                    list[i] = '+';
                    list[i+1] = '+';
                }
            }
        return false;
    }
}