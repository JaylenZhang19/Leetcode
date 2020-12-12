public class ZigzagIterator {
    List<Integer> l;
    int index = -1;
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        l = new ArrayList<>();
        int n = Math.max(v1.size(), v2.size());
        int c_pointer = 0;
        for(int i = 0; i < n; i++){
            if(i < v1.size()){
                l.add(v1.get(i));
            }
            if(i < v2.size()){
                l.add(v2.get(i));
            }
        }
    }

    public int next() {
        if(this.index + 1 < l.size()){
            return this.l.get(++this.index);
        }
        return -1;
    }

    public boolean hasNext() {
        return this.index + 1 < this.l.size();
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */