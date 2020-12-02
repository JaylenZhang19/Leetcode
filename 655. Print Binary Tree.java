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
    public List<List<String>> printTree(TreeNode root) {
        int[] values = find_depth_width(root);
        int depth = values[0];
        int width = values[1];
        List<List<String>> ret = new ArrayList<>();
        for(int row = 0; row < depth; row++){
            ret.add(new ArrayList<>());
            for(int col = 0; col < width; col++){
                ret.get(row).add("");
            }
        }
        helper(ret, 0, 0, width-1, root);
        return ret;
    }

    public int[] find_depth_width(TreeNode node){
        if(node == null){
            return new int[]{0, 0};
        }
        if(node.left == null && node.right == null){
            return new int[]{1, 1};
        }
        int[] left = find_depth_width(node.left);
        int[] right = find_depth_width(node.right);
        return new int[]{Math.max(left[0], right[0]) + 1, 2 * Math.max(left[1], right[1]) + 1};
    }

    public void helper(List<List<String>> ans, int depth, int left, int right, TreeNode root){
        int mid = left + (right - left) / 2;
        ans.get(depth).set(mid, root.val + "");
        if(root.left != null){
            helper(ans, depth + 1, left, mid-1, root.left);
        }
        if(root.right != null){
            helper(ans, depth+1, mid+1, right, root.right);
        }
    }
}