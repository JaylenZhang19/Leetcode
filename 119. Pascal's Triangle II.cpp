class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex == 0){
            return vector<int>{1};
        }
        if(rowIndex == 1){
            return vector<int>{1, 1};
        }
        vector<int> last_row = getRow(rowIndex - 1);
        vector<int> current_row {1};
        for(int start = 0; start < last_row.size() - 1; start++){
            current_row.push_back(last_row[start] + last_row[start + 1]);
        }
        current_row.push_back(1);
        return current_row;
    }
};