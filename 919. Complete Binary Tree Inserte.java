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
class CBTInserter {

    TreeNode head;
    Map<Integer, TreeNode> memo = new HashMap<>();
    int index = 0;
    public CBTInserter(TreeNode root) {
        head = root;
        Queue<TreeNode> queue = new ArrayDeque();
        queue.add(root);
        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            index += 1;
            if(node.left != null){
                queue.add(node.left);
            }
            if(node.right != null){
                queue.add(node.right);
            }
        }
    }

    public int insert(int v) {
        TreeNode node = new TreeNode(v);
        index += 1;
        if(index == 1){
            head = node;
            return -1;
        }
        int tmp = index / 2;
        Stack<Integer> stack = new Stack<>();
        while(tmp != 1){
            if(tmp % 2 == 1){
                stack.add(1);
            }else{
                stack.add(0);
            }
            tmp /= 2;
        }
        TreeNode par = head;
        while(!stack.isEmpty()){
            int state = stack.pop();
            if(state == 1){
                par = par.right;
            }
            else{
                par = par.left;
            }
            
        }
        if(index % 2 == 1){
            par.right = node;
        }
        else{
            par.left = node;
        }
        return par.val;
    }

    public TreeNode get_root() {
        return head;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */