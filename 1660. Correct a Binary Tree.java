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
    public TreeNode correctBinaryTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int invalid = Integer.MAX_VALUE;
        while(!queue.isEmpty() && invalid == Integer.MAX_VALUE){
            int size = queue.size();
            HashMap<Integer, Integer> parent = new HashMap<Integer, Integer>();
            for(int i = 0; i < size; i++){
                TreeNode current = queue.poll();
                if(parent.containsKey(current.val)){
                    invalid = parent.get(current.val);
                    break;
                }
                if(current.left != null){
                    queue.add(current.left);
                    parent.put(current.left.val, current.val);
                }
                if(current.right != null){
                    queue.add(current.right);
                    parent.put(current.right.val, current.val);
                }
            }
        }
        queue.clear();
        queue.add(root);
        while(!queue.isEmpty()){
            TreeNode current = queue.poll();
            if(current.left != null){
                if(current.left.val == invalid){
                    current.left = null;
                    break;
                }else{
                    queue.add(current.left);
                }
            }
            if(current.right != null){
                if(current.right.val == invalid){
                    current.right = null;
                    break;
                }else{
                    queue.add(current.right);
                }
            }
        }
        return root;
    }
    
}