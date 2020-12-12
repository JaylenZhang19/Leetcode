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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        boolean reverse = false;
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if(root == null){
            return ret;
        }
        List<TreeNode> l1 = new ArrayList<TreeNode>();
        l1.add(root);
        while(!l1.isEmpty()){
            List<TreeNode> l2 = new ArrayList<TreeNode>();
            List<Integer> retl1 = new ArrayList<Integer>();
            for(int i = 0; i < l1.size(); i++){
                TreeNode node = l1.get(i);
                retl1.add(node.val);
                if(node.left != null){
                    l2.add(node.left);
                }
                if(node.right != null){
                    l2.add(node.right);
                }
            }
            if(reverse){
                Collections.reverse(retl1);
                reverse = false;
            }else{
                reverse = true;
            }
            ret.add(retl1);
            l1 = l2;
        }
        return ret;
        
    }
}