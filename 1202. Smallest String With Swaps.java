class Solution {
    int[] id,sz;
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int n=s.length();
        id=new int[n];
        sz=new int[n];
        for (int i=0;i<n;i++){
            id[i]=i;
            sz[i]=1;
        }
        for (List<Integer> pair:pairs){
            int x=pair.get(0),y=pair.get(1);
            union(x,y);
        }

        HashMap<Integer,LinkedList<Character>> map=new HashMap<>();
        for (int i=0;i<s.length();i++){
            int r=root(i);
            map.putIfAbsent(r,new LinkedList<>());
            map.get(r).addLast(s.charAt(i));
        }
        for (int key:map.keySet()){
            Collections.sort(map.get(key));
        }
        StringBuilder sb=new StringBuilder();
        for (int i=0;i<s.length();i++){
            int r=root(i);
            sb.append(map.get(r).removeFirst());
        }
        return sb.toString();
    }

    public void union(int i,int j){
        int x=root(i),y=root(j);
        if (x==y) return;
        if (sz[x]<sz[y]){
            id[x]=y;
            sz[y]+=sz[x];
        }else{
            id[y]=x;
            sz[x]+=sz[y];
        }
    }

    public int root(int i){
        while (i!=id[i]){
            id[i]=id[id[i]];
            i=id[i];
        }
        return i;
    }
}