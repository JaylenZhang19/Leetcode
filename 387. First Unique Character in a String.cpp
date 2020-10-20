class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> counter;
        for(int i = 0; i < s.size(); i++){
            counter[s[i]]++;
        }
        for(int i = 0; i < s.size(); i++){
            if(counter[s[i]] == 1){
                return i;
            }
        }
        return -1;
    }
};