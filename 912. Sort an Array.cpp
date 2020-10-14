class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        merge_sort(nums, 0, nums.size()-1);
        return nums;
    }
    
    void merge_sort(vector<int>& nums, int start, int end){
        if(start == end){
            return ;
        }
        int mid = start + (end - start) / 2;
        merge_sort(nums,start, mid);
        merge_sort(nums, mid + 1, end);
        merge(nums, start, mid, end);
    }
    
    void merge(vector<int>& nums, int begin, int mid, int end){
        int i = begin, j = mid + 1;
        vector<int> tmp;
        while(i <= mid && j <= end){
            if(nums[i] <= nums[j]){
                tmp.push_back(nums[i]);
                i++;
            }else{
                tmp.push_back(nums[j]);
                j++;
            }
        }
        while(i <= mid){
            tmp.push_back(nums[i]);
            i++;
        }
        while(j <= end){
            tmp.push_back(nums[j]);
            j++;
        }
        for(int index = 0; index < tmp.size(); index++){
            nums[begin + index] = tmp[index]; 
        }
    }
};