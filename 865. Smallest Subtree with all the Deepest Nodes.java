/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int depth;
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        depth = find_depth(root);
        
        return helper(root, 0);
    }
    
    private TreeNode helper(TreeNode node, int current_depth){
        if(node == null){
            return null;
        }
        current_depth += 1;
        if(current_depth == depth){
            return node;
        }
        TreeNode left = helper(node.left, current_depth);
        TreeNode right = helper(node.right, current_depth);
        if(left != null & right != null){
            return node;
        }
        else if(left != null){
            return left;
        }
        else if(right != null){
            return right;
        }else{
            return null;
        }
        
    }
    
    private int find_depth(TreeNode root){
        if(root == null){
            return 0;
        }
        return Math.max(find_depth(root.left), find_depth(root.right)) + 1;
    }
}