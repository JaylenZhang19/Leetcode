class Solution {
    public int earliestAcq(int[][] logs, int N) {
        Arrays.sort(logs, (a, b)->a[0] - b[0]);
        int[] parent = new int[N];
        for(int i = 0; i < N; i++){
            parent[i] = i;
        }
        int[] size = new int[N];
        Arrays.fill(size, 1);
        for(int[] log : logs){
            int par1 = find(parent, log[1]);
            int par2 = find(parent, log[2]);
            if(par1 != par2){
                size[par1] += size[par2];
                parent[par2] = par1;
                if(size[par1] == N){
                    return log[0];
                }
            }
        }
        return -1;
    }

    private int find(int[] parent, int node){
        if(parent[node] == node){
            return node;
        }
        return find(parent, parent[node]);
    }

    private void union(int[] parent, int node1, int node2){
        int par1 = find(parent, node1);
        int par2 = find(parent, node2);
        parent[par1] = par2;
    }
}