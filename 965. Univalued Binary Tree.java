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
    public boolean isUnivalTree(TreeNode root) {
        if(root == null) return true;
        int val = root.val;
        Stack<TreeNode> stack = new Stack();
        while(!stack.isEmpty() || root != null){
            while(root != null){
                stack.add(root);
                root = root.left;
            }
            root = stack.pop();
            if(root.val != val) return false;
            root = root.right;
        }
        return true;
    }
}