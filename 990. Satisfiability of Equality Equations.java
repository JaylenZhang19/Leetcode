class Solution {
    public boolean equationsPossible(String[] equations) {
        int n = equations.length;
        int[] par = new int[26];
        for(int i = 0; i < 26; i++){
            par[i] = i;
        }

        for(String item : equations){
            if(item.charAt(1) == '='){
                union(par, item.charAt(0)-'a', item.charAt(3)-'a');
            }
        }
        for(String item : equations){
            if(item.charAt(1) == '!'){
                int par_a = find(par, item.charAt(0)-'a');
                int par_b = find(par, item.charAt(3)-'a');
                if (par_a == par_b){
                    return false;
                }
            }
        }
        return true;
    }
    public int find(int[] par, int c){
        if(par[c] == c){
            return c;
        }
        return find(par, par[c]);
    }

    public void union(int[] par, int a, int b){
        int par_a = find(par, a);
        int par_b = find(par, b);
        par[par_b] = par_a;
    }
}