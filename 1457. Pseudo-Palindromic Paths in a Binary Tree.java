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
    int ret = 0;
    public int pseudoPalindromicPaths (TreeNode root) {
        Map<Integer, Integer> counter = new HashMap<>();
        helper(root, 0, counter);
        return ret;
    }
    
    public void helper(TreeNode node, int odd, Map<Integer, Integer> counter){
        if(node == null){
            return;
        }
        counter.put(node.val, counter.getOrDefault(node.val, 0) + 1);
        if(counter.get(node.val) % 2 == 1){
            odd += 1;
        }
        else{
            odd -= 1;
        }
        if(node.left == null && node.right == null){
            if(odd <= 1){
                ret += 1;
            }
        }
        helper(node.left, odd, counter);
        helper(node.right, odd, counter);
        
        counter.put(node.val, counter.get(node.val) - 1);
    }
}