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
    bool isValidBST(TreeNode* root) {
        if(not root){
            return true;
        }
        return helper(root, LONG_MAX, LONG_MIN);
    }
    
    bool helper(TreeNode* root, long upper, long lower){
        if(root == NULL) return true;
        
        if(root -> val <= lower || root -> val >= upper) return false; 
        
        return helper(root->left, root->val, lower) && helper(root->right, upper, root->val); 
    }
};