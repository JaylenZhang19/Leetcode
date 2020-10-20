class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        vector<pair<int, int>> time_stamp;
        for(auto it1 : intervals){
            time_stamp.push_back(pair<int, int>{it1[0], 1});
            time_stamp.push_back(pair<int, int>{it1[1], 0});
        }
        sort(time_stamp.begin(), time_stamp.end());
        int ret = 0;
        int count = 0;
        for(auto it1 : time_stamp){
            if(it1.second == 1){
                count++;
            }else{
                count--;
            }
            ret = max(ret, count);
        }
        return ret;
    }
};