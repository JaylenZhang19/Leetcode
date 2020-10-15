class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        for(int r = 0; r < rows; r++){
            int left = 0, right = matrix[r].size() - 1;
            while(left <= right){
                int mid = left + (right - left) / 2;
                if (matrix[r][mid] == target){
                    return true;
                }
                else if (matrix[r][mid] < target){
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                }
            }
        }
        return false;
    }
};