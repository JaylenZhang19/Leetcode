/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n < 1){
            return vector<TreeNode*>();
        }
        return helper(1, n);
    }
    
    vector<TreeNode*> helper(int start, int end){
        vector<TreeNode*> ret;
        if (start > end) {
            ret.push_back(NULL);
            return ret;
        }
        for(int i = start; i <= end; i++){
            vector<TreeNode*> left = helper(start, i-1);
            vector<TreeNode*> right = helper(i + 1, end);
            for (auto l : left){
                for(auto r : right){
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    ret.push_back(root);
                }
            }
        }
        return ret;
    }
};