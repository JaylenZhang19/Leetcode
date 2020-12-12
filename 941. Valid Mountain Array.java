class Solution {
    public boolean validMountainArray(int[] arr) {
        boolean find1 = false;
        boolean find2 = false;
        int n = arr.length;
        if(n < 3){
            return false;
        }
        int index = 1;
        while(index < n && arr[index] > arr[index-1]){
            index ++;
            find1 = true;
        }

        while(index < n && arr[index] < arr[index-1]){
            index ++;
            find2 = true;
        }
        return find1 && find2 && index == n;
    }
}