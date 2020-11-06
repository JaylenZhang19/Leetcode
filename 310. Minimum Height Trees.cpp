class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n < 2){
            vector<int> ret;
            for(int i = 0; i < n; i++){
                ret.push_back(i);
            }
            return ret;
        }
        vector<set<int>> adj(n);
        for(auto edge : edges){
            adj[edge[0]].insert(edge[1]);
            adj[edge[1]].insert(edge[0]);
        }

        queue<int> q;
        for(int i = 0; i < n; i++){
            if(adj[i].size() == 1){
                q.push(i);
            }
        }

        while(n > 2){
            int len = q.size();
            n -= len;
            for(int count = 0; count < len; count++){
                int node = q.front();
                q.pop();

                for(auto it = adj[node].begin(); it != adj[node].end(); it++){
                    adj[*it].erase(node);
                    if(adj[*it].size() == 1){
                        q.push(*it);
                    }
                }

            }
        }
        vector<int> ret;
        while(not q.empty()){
            ret.push_back(q.front());
            q.pop();
        }
        return ret;
    }
};