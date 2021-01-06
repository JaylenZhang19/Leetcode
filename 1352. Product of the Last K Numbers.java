class ProductOfNumbers {
    ArrayList<Integer> list;
    public ProductOfNumbers() {
        list = new ArrayList();
    }

    public void add(int num){
        if(num == 0){
            list.clear();
        }
        else{
            list.add(list.size()>0?list.get(list.size() - 1) * num:num);
        }
    }

    public int getProduct(int k) {
        int n = list.size();
        if(k > n){
            return 0;
        }
        return list.get(n-1) / (n - k - 1 >= 0?list.get(n - k - 1) : 1);
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */