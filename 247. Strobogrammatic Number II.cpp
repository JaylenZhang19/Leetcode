class Solution {
public:
    vector<string> findStrobogrammatic(int n) {
        if (n == 0) {
            return {""};
        }
        if (n == 1) {
            return {"0", "1", "8"};
        }
        vector<string> res = findStrobo(n);
        vector<string> ret;
        if (n > 1) {
            for(int i = 0; i < res.size(); i++){
                if(res[i][0] != '0'){
                    ret.push_back(res[i]);
                }
            }
            
        }
        return ret;
        
    }
    vector<string> findStrobo(int n) {
        if (n == 0) {
            return {""};
        }
        if (n == 1) {
            return {"0", "1", "8"};
        }
        auto smaller = findStrobo(n - 2);
        vector<string> res;
        for (auto&& word : smaller) {
            res.emplace_back("0" + word + "0");
            res.emplace_back("1" + word + "1");
            res.emplace_back("6" + word + "9");
            res.emplace_back("8" + word + "8");
            res.emplace_back("9" + word + "6");
        }
        return res;
    }
};